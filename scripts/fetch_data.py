from pathlib import Path

RAW_DIR = Path("data/raw")

DATASETS = [
    # 把你们的CSV文件名在这里写死（强烈推荐）
    # {"name": "dataset1", "filename": "xxx.csv", "url": "https://..."},
]

def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    if not DATASETS:
        print("[fetch_data] No datasets configured yet.")
        print("Please download CSV files manually and place them into: data/raw/")
        return

    print("[fetch_data] Expected datasets:")
    for d in DATASETS:
        print(f"- {d['name']}: {d['filename']}")
        print(f"  url: {d['url']}")
        print(f"  save to: data/raw/{d['filename']}")

if __name__ == "__main__":
    main()
