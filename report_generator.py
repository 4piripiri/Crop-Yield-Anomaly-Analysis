"""
report_generator.py

Responsible for: pulling findings from the other modules into one written
report that connects the analysis back to the original problem statement.
Rubric criterion covered: Report Quality & Interpretation of Results.
"""

from pathlib import Path

REPORTS_DIR = Path(__file__).resolve().parent.parent / "outputs" / "reports"


def generate_report(anomaly_years: list, correlations: dict, forecast=None, save_as: str = "report.md") -> None:
    """
    Write a markdown report summarizing:
      1. Which years were flagged as anomalously poor yield
      2. Which factor(s) correlated most strongly with those dips (with r and p-value)
      3. What the forecast suggests for future years
      4. A concluding interpretation tying it back to the problem statement

    TODO: flesh this out into full prose once the other modules produce real
    results — this is the section the rubric weighs on "connecting analysis
    back to the problem statement", not just listing numbers.
    """
    lines = [
        "# Crop Yield Anomaly Report",
        "",
        "## Anomalous Poor-Yield Years",
        f"{anomaly_years}",
        "",
        "## Correlation with Environmental Factors",
        f"{correlations}",
        "",
        "## Forecast",
        f"{forecast}",
        "",
        "## Interpretation",
        "TODO: write 2-3 paragraphs connecting the above back to the problem statement.",
    ]
    (REPORTS_DIR / save_as).write_text("\n".join(lines))
    print(f"Report written to {REPORTS_DIR / save_as}")
