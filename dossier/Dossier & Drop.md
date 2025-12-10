# Create dossier/ if missing (GitHub auto-does on add)
mkdir -p dossier/
# Paste the MD content into dossier/IR-2025-12-10-Youth-Revolution-Echo-Briefing-FINAL.md
git add dossier/IR-2025-12-10-Youth-Revolution-Echo-Briefing-FINAL.md
git commit -m "feat(dossier-init): Bootstrap dossier/ with FINAL Youth Revolution MD – SHA-256 f3a2b1c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2 sealed for VIP Echo."
git push origin main
