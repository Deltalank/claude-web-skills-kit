#!/usr/bin/env bash
set -euo pipefail

mkdir -p dist

for skill_dir in skills/*; do
  if [ -d "$skill_dir" ] && [ -f "$skill_dir/SKILL.md" ]; then
    skill_name="$(basename "$skill_dir")"
    echo "Packaging $skill_name..."
    (
      cd skills
      zip -r "../dist/${skill_name}.zip" "$skill_name" -x "*/.DS_Store"
    )
  fi
done

echo "Skill ZIP files created in dist/"
