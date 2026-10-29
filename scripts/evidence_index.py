#!/usr/bin/env python3
"""Create a private, local-only SHA-256 evidence index. Never uploads files.

Usage: python3 evidence_index.py /private/originals --output /private/index.json
Output filenames can disclose personal data. Do not publish the index unchanged.
Hashes demonstrate byte identity, not authenticity, capture date or admissibility.
"""
import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path


def build_index(root):
    root = Path(root)
    if root.is_symlink() or not root.is_dir():
        raise ValueError('Evidence root must be a real directory, not a symlink')
    root = root.resolve()
    result = []
    for folder, dirs, names in os.walk(root, followlinks=False):
        for name in dirs + names:
            if (Path(folder) / name).is_symlink():
                raise ValueError('Symlinks are not supported; use an explicit evidence-only folder')
        dirs.sort()
        for name in sorted(names):
            path = Path(folder) / name
            if not path.is_file():
                raise ValueError('Non-regular evidence entry is not supported')
            before = path.stat()
            digest = hashlib.sha256()
            with path.open('rb') as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                    digest.update(chunk)
            after = path.stat()
            if (before.st_size, before.st_mtime_ns, before.st_ino) != (after.st_size, after.st_mtime_ns, after.st_ino):
                raise ValueError('Evidence changed during hashing; no index was saved')
            result.append({'path': path.relative_to(root).as_posix(), 'bytes': after.st_size, 'sha256': digest.hexdigest()})
    return {'schema_version': 1, 'generated_at_utc': datetime.now(timezone.utc).isoformat(),
            'warning': 'PRIVATE: filenames may identify people. Hashes are not proof of authenticity.',
            'files': sorted(result, key=lambda row: row['path'])}


def write_index(root, output):
    root, output = Path(root), Path(output)
    if output.is_symlink():
        raise ValueError('Output must not be a symlink')
    resolved_root, resolved_output = root.resolve(), output.resolve()
    if resolved_output == resolved_root or resolved_root in resolved_output.parents:
        raise ValueError('Output must be outside the evidence folder')
    result = build_index(root)
    # Exclusive creation preserves previous indices and prevents accidental overwrite.
    with output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    try:
        result = write_index(args.root, args.output)
    except (OSError, ValueError) as error:
        parser.exit(1, f'No usable index created: {error}\n')
    print(f"Indexed {len(result['files'])} files locally. Keep the index private; no files uploaded.")


if __name__ == '__main__':
    main()
