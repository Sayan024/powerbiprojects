import os
import shutil
import subprocess

def run(cmd):
    print(f"Running: {cmd}")
    res = subprocess.run(cmd, shell=True, cwd=r"D:\Practise Coding Files\powerbi\dashboards", capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)
    return res

branches_map = {
    "Dine360RestuarantAnalysis": "Rseturant Sales",
    "Shoperkart": "Shoperkart",
    "VoltSalesDashboard": "volt"
}

repo_dir = r"D:\Practise Coding Files\powerbi\dashboards"

for branch, subfolder in branches_map.items():
    print(f"\n==========================================")
    print(f"Processing branch: {branch} (subfolder: {subfolder})")
    print(f"==========================================")
    
    # Checkout branch with force
    run(f"git checkout -f {branch}")
    
    subfolder_path = os.path.join(repo_dir, subfolder)
    if os.path.exists(subfolder_path):
        # Move all items inside subfolder_path to repo_dir
        for item in os.listdir(subfolder_path):
            src = os.path.join(subfolder_path, item)
            dst = os.path.join(repo_dir, item)
            print(f"Moving {src} -> {dst}")
            if os.path.exists(dst):
                if os.path.isdir(dst):
                    shutil.rmtree(dst)
                else:
                    os.remove(dst)
            shutil.move(src, dst)
        
        # Remove empty subfolder
        try:
            os.rmdir(subfolder_path)
        except Exception as e:
            print(f"Could not remove subfolder: {e}")
            shutil.rmtree(subfolder_path, ignore_errors=True)
            
    # Add all files, commit and push
    run("git add -A")
    run(f'git commit -m "refactor: move {subfolder} project files to root level of {branch}"')
    run(f"git push origin {branch}")

# Switch back to main
run("git checkout -f main")
print("Done!")
