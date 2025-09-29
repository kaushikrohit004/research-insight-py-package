import sys
import os
import pandas as pd

package_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if package_path not in sys.path:
    sys.path.insert(0, package_path)

from research_insight import analyze

def main():
    print("Running tests...\n")

    df = pd.DataFrame({"A":[1,2,3], "B":[4,5,6]})
    report = analyze(df)
    summary = report.summary()
    print("Summary:\n", summary)
    assert "A" in summary.columns
    assert "B" in summary.columns
    print("Summary test passed\n")

    df2 = pd.DataFrame({"A":[1,None,3], "B":[4,5,None]})
    report2 = analyze(df2)
    missing = report2.missing_report()
    print("Missing report:\n", missing)
    assert missing["A"] == 1 and missing["B"] == 1
    print("Missing report test passed\n")

    df3 = pd.DataFrame({"X":[1,2,3,4], "Y":[4,3,2,1]})
    report3 = analyze(df3)
    try:
        report3.plot_correlations()
        print("Correlation plot ran without error\n")
    except Exception as e:
        print("Correlation plot failed:", e)
        return

    print("All tests passed!")

if __name__ == "__main__":
    main()
