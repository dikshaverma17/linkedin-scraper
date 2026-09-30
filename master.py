import subprocess
import sys
from pathlib import Path


# ============================================================
# LINKEDIN COMPLETE PIPELINE
# ============================================================
# Run this file with:
#     python pipeline_master.py
#
# It runs the four existing stages in this order:
# 1. login_use.py
# 2. filter_education.py
# 3. main.py
# 4. scraper_authenticated.py
#
# All stages use the same project folder and existing files.
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

STAGES = [
    ("STAGE 1 - LINKEDIN LOGIN", "login_use.py"),
    ("STAGE 2 - EDUCATION EXTRACTION", "filter_education.py"),
    ("STAGE 3 - UG -> FOREIGN PG FILTER", "main.py"),
    ("STAGE 4 - FINAL PROFILE SCRAPER", "scraper_authenticated.py"),
]


def run_stage(stage_name, script_name):
    script_path = BASE_DIR / script_name

    print("\n")
    print("=" * 80)
    print(stage_name)
    print("=" * 80)
    print(f"[RUNNING] {script_name}")
    print("=" * 80)

    if not script_path.exists():
        print(f"[ERROR] File not found: {script_path}")
        return False

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(BASE_DIR),
    )

    if result.returncode != 0:
        print("\n" + "=" * 80)
        print(f"[FAILED] {script_name}")
        print(f"[EXIT CODE] {result.returncode}")
        print("=" * 80)
        return False

    print("\n" + "=" * 80)
    print(f"[COMPLETED] {script_name}")
    print("=" * 80)

    return True


def main():
    print("\n" + "=" * 80)
    print("LINKEDIN COMPLETE AUTOMATED PIPELINE")
    print("=" * 80)
    print(f"[PROJECT] {BASE_DIR}")
    print("=" * 80)

    for stage_name, script_name in STAGES:
        success = run_stage(stage_name, script_name)

        if not success:
            print("\n" + "=" * 80)
            print("PIPELINE STOPPED")
            print("=" * 80)
            print(f"Failed stage: {script_name}")
            print("Fix the error above and run the master file again.")
            print("=" * 80)
            sys.exit(1)

    print("\n" + "=" * 80)
    print("ALL 4 STAGES COMPLETED SUCCESSFULLY")
    print("=" * 80)
    print("\nFinal files you should have:")
    print("  - storage_state.json")
    print("  - education_extracted.txt {where you can find the extracted education details}")
    print("  - selected_urls.json {where you can find the filtered profile URLs}")
    print("  - extracted_profiles.txt {where you can find the extracted profile data}")
    print("  - profile_errors.txt {where you can find any errors that occurred during scraping}")
    print("=" * 80)


if __name__ == "__main__":
    main()
