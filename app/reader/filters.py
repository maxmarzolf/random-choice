from datetime import datetime

from . import reader_bp


@reader_bp.app_template_filter('display_date')
def display_date(dt):
    diff = datetime.now() - dt
    print(diff)

    if diff.days <= 1:
        return "Today"
    else:
        # return f"{dt.month} {dt.day}, {dt.year}"
        return dt.strftime("%d %B %Y")

@reader_bp.app_template_filter('strip_p_tag')
def strip_p_tags(paragraph):
    if paragraph[0:3] == '<p>':
        paragraph = paragraph[3:]
    
    if paragraph[-4:] == '</p>':
        paragraph = paragraph[:-4]
    
    return paragraph

# NEED: A filter that closes all tags in the order they were opened.