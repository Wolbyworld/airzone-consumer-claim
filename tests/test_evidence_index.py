"""Synthetic local-only tests. Run: python3 -m unittest discover -s tests -v"""
import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path

path = Path(__file__).resolve().parents[1] / 'scripts' / 'evidence_index.py'
spec = importlib.util.spec_from_file_location('evidence_index', path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class EvidenceIndexTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.root = self.base / 'originals'
        self.root.mkdir()
        (self.root / 'synthetic.txt').write_bytes(b'synthetic evidence\n')
    def tearDown(self):
        self.temp.cleanup()
    def test_exact_hash_and_unchanged_original(self):
        data = module.write_index(self.root, self.base / 'index.json')
        self.assertEqual(data['files'], [{'path':'synthetic.txt', 'bytes':19, 'sha256':hashlib.sha256(b'synthetic evidence\n').hexdigest()}])
        self.assertEqual((self.root / 'synthetic.txt').read_bytes(), b'synthetic evidence\n')
    def test_no_overwrite(self):
        output = self.base / 'index.json'
        output.write_text('existing')
        with self.assertRaises(FileExistsError): module.write_index(self.root, output)
        self.assertEqual(output.read_text(), 'existing')
    def test_output_cannot_contaminate_evidence(self):
        with self.assertRaises(ValueError): module.write_index(self.root, self.root / 'index.json')
        self.assertFalse((self.root / 'index.json').exists())
    def test_symlink_rejected(self):
        (self.root / 'link').symlink_to(self.root / 'synthetic.txt')
        with self.assertRaises(ValueError): module.write_index(self.root, self.base / 'index.json')
        self.assertFalse((self.base / 'index.json').exists())
    def test_missing_root(self):
        with self.assertRaises(ValueError): module.write_index(self.base / 'missing', self.base / 'index.json')

if __name__ == '__main__': unittest.main()
