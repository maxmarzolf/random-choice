from datetime import datetime

from . import reader_bp

@reader_bp.app_template_filter('display_date')
def display_date(dt):
    diff = datetime.now() - dt
    print(diff)

    if diff.days <= 1:
        return "Today"
    else:
        #return f"{dt.month} {dt.day}, {dt.year}"
        return dt.strftime("%d %B %Y")