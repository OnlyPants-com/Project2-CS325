import subprocess
import sys
import os

class JobMatcher:
    """Class to run the full job matching pipeline.""" 
    def run_full_pipeline(self):
        
        print("=" * 60)
        print("JOB MATCHER - Full Pipeline")
        print("=" * 60)
        
        # Scripts are in src/ folder - use os.path.join for Windows compatibility
        steps = [
            ("Fetching jobs from Adzuna...", os.path.join("src", "getdata.py")),
            ("Preprocessing data...", os.path.join("src", "preprocess.py")),
            ("Generating embeddings...", os.path.join("src", "embedding.py")),
            ("Calculating similarities...", os.path.join("src", "similarity.py"))
        ]
        
        for step_name, script in steps:
            print(f"\n{step_name}")
            try:
                result = subprocess.run(
                    [sys.executable, script],
                    check=True,
                    capture_output=True,
                    text=True,
                    cwd=os.getcwd()  # Run from project root
                )
                print(result.stdout)
                if result.stderr:
                    print("Warnings:", result.stderr)
            except subprocess.CalledProcessError as e:
                print(f"Error running {script}: {e}")
                print("STDOUT:", e.stdout)
                print("STDERR:", e.stderr)
                sys.exit(1)
            except FileNotFoundError:
                print(f"ERROR: Could not find {script}")
                print(f"Current directory: {os.getcwd()}")
                print(f"Make sure you're running from the project root directory")
                sys.exit(1)
        
        print("\n" + "=" * 60)
        print("Pipeline complete!")
        print("=" * 60)


def main():
    matcher = JobMatcher()
    matcher.run_full_pipeline()


if __name__ == "__main__":
    main()