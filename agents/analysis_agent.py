import os


class AnalysisAgent:
    def generate_report(self, recommendations):
        try:
            report_path = "investment_report.html"
            with open(report_path, "w", encoding="utf-8") as f:
                f.write("<html><head><title>Investment Report</title></head><body>")
                f.write("<h1>📊 Investment Recommendations</h1>")

                if not recommendations:
                    f.write("<p>No suitable investment opportunities found.</p>")
                else:
                    for rec in recommendations:
                        f.write(f"<h2>{rec['title']}</h2>")
                        f.write(f"<p><strong>Sentiment:</strong> {rec['sentiment']}</p>")
                        f.write(f"<p><strong>Recommendation:</strong> {rec['strategy']}</p>")
                        f.write(f"<p><a href='{rec['url']}' target='_blank'>🔗 View Source</a></p><hr>")

                f.write("</body></html>")

            print(f"✅ Report generated: {report_path}")
        except Exception as e:
            print(f"❌ Error in report generation: {e}")
