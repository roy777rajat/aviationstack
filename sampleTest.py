import json
import webbrowser
import tempfile

# Sample JSON list
json_data = '''
[
    {"name": "John Doe", "email": "john.doe@example.com", "role": "Developer", "joined": "2023-06-15"},
    {"name": "Jane Smith", "email": "jane.smith@example.com", "role": "Designer", "joined": "2022-11-20"},
    {"name": "Alice Brown", "email": "alice.brown@example.com", "role": "Manager", "joined": "2021-09-01"}
]
'''

# Your actual social profile links
linkedin_url = "https://www.linkedin.com/in/yourprofile"
medium_url = "https://medium.com/@yourprofile"
facebook_url = "https://facebook.com/yourprofile"

# Icon URLs (SVGs or PNGs with transparent background)
linkedin_icon = "https://cdn-icons-png.flaticon.com/512/174/174857.png"
medium_icon = "https://cdn-icons-png.flaticon.com/512/5968/5968885.png"
facebook_icon = "https://cdn-icons-png.flaticon.com/512/733/733547.png"

# Parse JSON
rows = json.loads(json_data)
headers = rows[0].keys()

# Emirates logo URL
logo_url = "https://upload.wikimedia.org/wikipedia/commons/4/4b/Emirates_logo.svg"

# Generate HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Emirates Staff Directory</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f7fa;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }}
        .header {{
            display: flex;
            align-items: center;
            background-color: #d71920;
            color: white;
            padding: 1rem 2rem;
        }}
        .header img {{
            height: 50px;
            margin-right: 1rem;
        }}
        .header h1 {{
            margin: 0;
            font-size: 1.5rem;
        }}
        .table-container {{
            flex-grow: 1;
            padding: 1rem;
            display: flex;
            justify-content: center;
        }}
        table {{
            width: 100%;
            max-width: 1000px;
            border-collapse: separate;
            border-spacing: 0 10px;
        }}
        thead {{
            display: none;
        }}
        tr {{
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            margin-bottom: 10px;
            display: block;
            padding: 1rem;
            text-align: center;
        }}
        tbody tr:nth-child(even) {{
            background-color: #f0f4f8;
        }}
        td {{
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 0.5rem 1rem;
            border-bottom: 1px solid #eee;
            font-size: 0.95rem;
        }}
        td:last-child {{
            border-bottom: none;
        }}
        td::before {{
            content: attr(data-label);
            font-weight: bold;
            color: #333;
            margin-right: 10px;
        }}
        @media (min-width: 768px) {{
            thead {{
                display: table-header-group;
            }}
            tr {{
                display: table-row;
                text-align: center;
                box-shadow: none;
                border: 1px solid #ddd;
            }}
            td {{
                display: table-cell;
                padding: 1rem;
            }}
            td::before {{
                content: "";
                display: none;
            }}
        }}
        .footer {{
            background-color: #f0f0f0;
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: #555;
        }}
        .footer a {{
            margin: 0 10px;
            display: inline-block;
        }}
        .footer img {{
            width: 28px;
            height: 28px;
            vertical-align: middle;
        }}
    </style>
</head>
<body>
    <div class="header">
        <img src="{logo_url}" alt="Emirates Logo">
        <h1>Emirates Staff Directory</h1>
    </div>
    <div class="table-container">
        <table>
            <thead>
                <tr>{"".join(f"<th>{header.title()}</th>" for header in headers)}</tr>
            </thead>
            <tbody>
                {"".join(
                    "<tr>" + "".join(
                        f'<td data-label="{header.title()}">{row[header]}</td>' 
                        for header in headers) + "</tr>"
                    for row in rows
                )}
            </tbody>
        </table>
    </div>
    <div class="footer">
        <span>Connect with me:</span><br>
        <a href="{linkedin_url}" target="_blank" title="LinkedIn"><img src="{linkedin_icon}" alt="LinkedIn"></a>
        <a href="{medium_url}" target="_blank" title="Medium"><img src="{medium_icon}" alt="Medium"></a>
        <a href="{facebook_url}" target="_blank" title="Facebook"><img src="{facebook_icon}" alt="Facebook"></a>
    </div>
</body>
</html>
"""

# Write to a temporary HTML file and open in browser
with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as f:
    f.write(html_content)
    webbrowser.open('file://' + f.name)


# The above code generates a simple HTML table from a JSON list and opens it in the default web browser.
#Define main function
def main():
    # Call the function to generate and display the HTML table
    pass  # The code above already handles this