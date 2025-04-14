from .utils import get_content_using_link

def store_job_description(document_link):
    try:
        # Get the content using the document link.
        content = get_content_using_link(document_link)
        
        # Summarize the content.
        # Store the content.
    except Exception as e:
        raise e