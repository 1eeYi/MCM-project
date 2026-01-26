from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")
OUT_DIR = Path("data/processed")

# 你们把“必须存在的原始文件名”写在这里
REQUIRED_FILES = [
    # "xxx.csv",
]

def require_files():
    missing = [f for f in REQUIRED_FILES if not (RAW_DIR / f).exists()]
    if missing:
        raise FileNotFoundError(
            "Missing raw CSV files:\n"
            + "\n".join([f"- data/raw/{m}" for m in missing])
            + "\n\nDownload them (see DATA_SOURCES.md) and place into data/raw/."
        )

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if not REQUIRED_FILES:
        print("[clean_data] REQUIRED_FILES is empty. Configure it with your CSV filenames.")
        print("[clean_data] Nothing to do.")
        return

    require_files()

    # 示例：把多个CSV读进来后，按你们需要合并/筛选
    cleaned = {}
    for fn in REQUIRED_FILES:
        df = pd.read_csv(RAW_DIR / fn)
        # 数据很干净的话，这里可以只做字段名统一、类型转换、去空格等轻量处理
        df.columns = [c.strip() for c in df.columns]
        cleaned[fn] = df
        print(f"[clean_data] loaded {fn}: {df.shape}")

    # 示例：只输出一个“汇总文件”，你们也可以分别输出
    # 这里先输出一个简单的 manifest，避免你们一上来就纠结合并逻辑
    manifest = pd.DataFrame(
        [{"file": k, "rows": v.shape[0], "cols": v.shape[1]} for k, v in cleaned.items()]
    )
    manifest.to_csv(OUT_DIR / "manifest.csv", index=False)
    print("[clean_data] wrote data/processed/manifest.csv")

if __name__ == "__main__":
    main()

