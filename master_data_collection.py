

import subprocess


scripts = [
    
    "FinSight\\data\\technical_indicators\\collect_CCI.py",
    
      
]

def main():
    for script in scripts:
        try:
            print(f"Executing {script}...")
            subprocess.check_call(['python', script])
            print(f"Finished executing {script}.\n")
        except subprocess.CalledProcessError:
            print(f"Error occurred while executing {script}!")
            
if __name__ == "__main__":
    main()
