from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

# --------------------------------------------------------
# SSISM Integrity Block — Single File Generator
# --------------------------------------------------------

filename = "SSISM_Integrity_Block_Template.pdf"

styles = getSampleStyleSheet()
style = styles['Normal']

text = """
SSISM INTEGRITY & METADATA BLOCK
Version: SSISM-IMB-2025-Dec-08
Classification: SSISM Threat Intelligence – Public Release

Document Title:
<INSERT TITLE HERE>

Document ID:
<INSERT DOCUMENT ID HERE>

Author/Unit:
SSISM Threat Intelligence Unit (T.I.U.)

Publisher:
SSISM Dissemination Engine V1
GitHub Project: UIngarsoe / SSISM_DISSEMINATION_ENGINE_V1

Timestamp (UTC+7):
<INSERT TIMESTAMP HERE>

Hash Algorithm:
SHA-256 (FIPS 180-4 Certified)

SHA-256 Checksum:
<INSERT AFTER FINAL UPLOAD>

Integrity Notes:
- This checksum confirms file immutability post-upload.
- Any alteration will produce a mismatched digest.
- Original publication chain stored across:
  • GitHub Commit Tree
  • SSISM IPFS Immortality Seal
  • Local Archive Node (Author)

Integrity Officer:
SSISM-TIU / Automated Integrity Module v1.8

---------------------------------------------------------
PLACEHOLDER FOR FULL REPORT CONTENT
(Replace this section with the final report text before hashing.)
"""

doc = SimpleDocTemplate(filename, pagesize=A4)
story = []

for line in text.split("\n"):
    story.append(Paragraph(line, style))
    story.append(Spacer(1, 4*mm))

doc.build(story)

print("Generated:", filename)
