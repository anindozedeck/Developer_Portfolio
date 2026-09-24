import calendar
import html
import webbrowser
from pathlib import Path


YEAR = 2027
OUTPUT_FILE = Path(__file__).with_name(f"calendar_{YEAR}.html")


def month_markup(month_number):
	month_calendar = calendar.Calendar(firstweekday=calendar.SUNDAY).monthdayscalendar(
		YEAR, month_number
	)
	day_cells = []

	for week in month_calendar:
		for day in week:
			if day == 0:
				day_cells.append('<span class="day empty"></span>')
				continue

			classes = ["day"]
			if calendar.weekday(YEAR, month_number, day) >= 5:
				classes.append("weekend")
			if month_number == 1 and day == 1:
				classes.append("new-year")

			day_cells.append(
				f'<span class="{" ".join(classes)}">{day}</span>'
			)

	return f"""
		<article class="month">
			<h2>{html.escape(calendar.month_name[month_number])}</h2>
			<div class="weekdays">{''.join(f'<span>{day}</span>' for day in calendar.day_abbr)}</div>
			<div class="days">{''.join(day_cells)}</div>
		</article>
	"""


def build_calendar_page():
	months = "".join(month_markup(month_number) for month_number in range(1, 13))
	return f"""<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>{YEAR} Calendar</title>
	<style>
		:root {{
			--ink: #17212b;
			--muted: #65727e;
			--paper: #f7f4ed;
			--card: #fffdf8;
			--accent: #d95f39;
			--line: #e5ded2;
		}}

		* {{ box-sizing: border-box; }}

		body {{
			margin: 0;
			color: var(--ink);
			background: radial-gradient(circle at top right, #f3d6bc 0, transparent 32rem), var(--paper);
			font-family: Georgia, "Times New Roman", serif;
		}}

		header {{
			max-width: 1400px;
			margin: 0 auto;
			padding: 4rem 2rem 2rem;
		}}

		.eyebrow {{
			margin: 0 0 .5rem;
			color: var(--accent);
			font: 700 .75rem/1.2 Arial, sans-serif;
			letter-spacing: .16em;
			text-transform: uppercase;
		}}

		h1 {{
			margin: 0;
			font-size: clamp(3.5rem, 9vw, 8rem);
			line-height: .85;
			letter-spacing: -.04em;
		}}

		.subtitle {{
			max-width: 32rem;
			margin: 1.5rem 0 0;
			color: var(--muted);
			font: 1rem/1.5 Arial, sans-serif;
		}}

		main {{
			display: grid;
			grid-template-columns: repeat(3, minmax(0, 1fr));
			gap: 1.25rem;
			max-width: 1400px;
			margin: 0 auto;
			padding: 1rem 2rem 4rem;
		}}

		.month {{
			padding: 1.25rem;
			background: var(--card);
			border: 1px solid var(--line);
			box-shadow: 0 1rem 2rem rgb(92 68 42 / 7%);
		}}

		h2 {{ margin: 0 0 1rem; font-size: 1.65rem; }}

		.weekdays, .days {{
			display: grid;
			grid-template-columns: repeat(7, 1fr);
			gap: .3rem;
			text-align: center;
		}}

		.weekdays {{
			padding-bottom: .6rem;
			color: var(--muted);
			font: 700 .68rem Arial, sans-serif;
			text-transform: uppercase;
		}}

		.day {{
			display: grid;
			place-items: center;
			aspect-ratio: 1;
			border-radius: 50%;
			font: .9rem Arial, sans-serif;
		}}

		.day.weekend {{ color: var(--accent); }}
		.day.new-year {{ color: white; background: var(--accent); font-weight: 700; }}

		@media (max-width: 900px) {{
			main {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
		}}

		@media (max-width: 580px) {{
			header {{ padding: 2.5rem 1rem 1rem; }}
			main {{ grid-template-columns: 1fr; padding: 1rem 1rem 2rem; }}
			h1 {{ font-size: 5rem; }}
		}}
	</style>
</head>
<body>
	<header>
		<p class="eyebrow">A year in view</p>
		<h1>{YEAR}</h1>
		<p class="subtitle">All twelve months, arranged for a quick scan on desktop or mobile.</p>
	</header>
	<main>{months}</main>
</body>
</html>
"""


if __name__ == "__main__":
	OUTPUT_FILE.write_text(build_calendar_page(), encoding="utf-8")
	webbrowser.open_new_tab(OUTPUT_FILE.resolve().as_uri())
	print(f"Generated and opened: {OUTPUT_FILE}")