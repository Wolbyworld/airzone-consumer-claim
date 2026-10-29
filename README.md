# Airzone Cloud: guía para documentar cambios y reclamar

Una guía y una **skill portátil para agentes** que ayuda a propietarios de Airzone a organizar pruebas, entender qué condiciones afectan a su equipo y preparar una reclamación individual, clara y proporcionada.

**Proyecto independiente.** No está afiliado, respaldado ni dirigido por Airzone, OCU, una administración de consumo o un despacho de abogados. Ofrece información general, **no asesoramiento jurídico individual**, y no garantiza un resultado. No afirma que toda suscripción sea ilegal ni que todos los equipos hayan perdido funciones.

## Empieza aquí

- **Soy propietario:** lee la [guía de una página](assets/quick-start-es.md). Identifica tu modelo, país, fecha de compra y la función que te preocupa. No publiques tus documentos personales.
- **Soy un agente:** carga [SKILL.md](SKILL.md) y consulta solo las referencias necesarias. Trabaja con los documentos del titular en un espacio privado; enseña la versión final antes de cualquier envío o publicación.
- **Ya reclamé:** revisa la [guía de seguimiento](references/filing-followthrough.md) antes de repetir una presentación. Un error o timeout no demuestra que el registro haya fallado.
- **Quiero informar a otros:** usa el [kit de difusión](assets/campaign-kit-es.md) como borrador factual, no como una campaña ya autorizada ni como una denuncia universal.

No se instala nada automáticamente. Un agente que no admita skills puede leer los mismos archivos como instrucciones y plantillas. El agente debe respetar sus propias reglas de seguridad y permisos.

## Qué contiene

| Recurso | Para qué sirve |
|---|---|
| [SKILL.md](SKILL.md) | Flujo completo, límites de autorización y criterios de calidad |
| [Intake y pruebas](references/intake-evidence.md) | Modelo, contrato, hechos, lagunas y protección de originales |
| [Registro del caso](assets/case-file.md) | Cronología, pruebas, aprobaciones y justificantes; rellenar solo en privado |
| [Reclamación a la empresa](assets/company-claim-es.md) | Solicitud concreta con base documental |
| [Análisis de respuesta](references/reply-analysis.md) y [réplica](assets/reply-followup-es.md) | Distinguir lo contestado de las preguntas pendientes |
| [Borrador para Consumo](assets/consumo-filing-es.md) | Preparación de intermediación, no presentación automática |
| [Fuentes y marco jurídico](references/sources-and-law.md) | Puntos de partida oficiales y cuestiones que requieren verificación |
| [Difusión y privacidad](references/campaign-privacy.md) | Comunicación veraz, opt-in y revisión de materiales |
| [Ejemplo sintético](assets/synthetic-example.md) | Aprender sin utilizar el expediente de otra persona |

La ruta jurídica desarrollada se centra en **España**, con un ejemplo de procedimiento de la **Comunidad de Madrid**. No debe aplicarse automáticamente a otros países, comunidades autónomas, compras profesionales o cadenas contractuales diferentes.

## Lo que debe comprobarse en cada caso

La base de investigación se revisó el **29 de octubre de 2026**. Antes de actuar, verifica las fuentes oficiales y el estado real del equipo: las condiciones, los precios y los procedimientos pueden cambiar.

- Un cambio **anunciado** no es lo mismo que una función **ya restringida** o un **cargo realizado**.
- Hay excepciones según el modelo y la fecha, especialmente en Aidoo. No se trasladan automáticamente a Webserver o HUB.
- Las condiciones públicas actuales no prueban qué versión aceptó el propietario.
- El vendedor, el instalador, el fabricante y el prestador de Cloud pueden ser entidades diferentes.
- Una prueba gratuita no aclara por sí sola qué funciones permanecerán disponibles después.
- Una reclamación a la empresa, un informe a OCU, una intermediación administrativa y un arbitraje son vías diferentes. El arbitraje puede ser vinculante.

Consulta las [condiciones oficiales del plan](https://support.airzonecloud.com/#/support/PLAN_CLOUD/content/CLOUD_PLAN_CONDITIONS), la [tabla de funciones](https://support.airzonecloud.com/#/support/PLAN_CLOUD/content/CLOUD_PLAN_FUNCTIONS), las [condiciones específicas de Aidoo](https://support.airzonecloud.com/#/support/PLAN_CLOUD/content/CLOUD_PLAN_AIDOOFUNCTIONS) y el [mapa de fuentes](references/sources-and-law.md).

## Privacidad: este repositorio no recibe expedientes

**No subas facturas, correos privados, DNI/NIE, direcciones, firmas, números de expediente, justificantes, códigos QR, identificadores de dispositivos ni datos de terceros.** Tampoco deben añadirse en pull requests, comentarios, ejemplos o archivos de prueba.

No publiques materiales privados o de terceros por el mero hecho de estar anonimizados. Cualquier extracto propuesto requiere una revisión separada de privacidad, confidencialidad, derechos de reproducción y exactitud contextual, además de autorización para su difusión. La opción preferente es un resumen propio neutral y enlaces a fuentes oficiales públicas.

Este proyecto contiene documentación y una herramienta local. **No incluye formularios, recogida de archivos, analítica, seguimiento de visitantes ni un servicio de reclamaciones.** No envía quejas, no inicia suscripciones y no representa a propietarios. No promueve quejas falsas, duplicadas, spam ni campañas de valoraciones coordinadas.

## Herramienta local opcional

Con Python 3, puedes generar un índice SHA-256 de una carpeta de pruebas **privada**:

```bash
python3 scripts/evidence_index.py /ruta/privada/originals --output /ruta/privada/index.json
```

No sube archivos, no modifica los originales y no sobrescribe un índice existente. Los nombres del índice también pueden contener datos personales: mantenlo privado. Un hash permite comparar bytes, pero no prueba autenticidad, fecha de captura ni admisibilidad jurídica.

Pruebas locales con archivos sintéticos temporales:

```bash
python3 -m unittest discover -s tests -v
```

## Correcciones documentales

Las mejoras deben limitarse a instrucciones, plantillas, ejemplos inequívocamente sintéticos y fuentes públicas verificables. No aportes expedientes reales para demostrar un problema. Antes de cualquier publicación propia, revisa hechos, excepciones, fuentes, permisos y audiencia.

## Licencia

Todavía no se ha elegido una licencia de reutilización. No se incluye un archivo `LICENSE` ni se presenta esta publicación como un proyecto de código abierto con licencia. La elección de licencia queda pendiente del titular del repositorio.
