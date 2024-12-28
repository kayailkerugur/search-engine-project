import os
from datetime import datetime
import psycopg2
from psycopg2.extras import Json
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

def save_search_results(query, results):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("""
            INSERT INTO search_history (query, search_date)
            VALUES (%s, %s)
            RETURNING id
        """, (query, datetime.now()))
        
        search_id = cur.fetchone()[0]
        
        if isinstance(results, list):
            items = results  # Eğer direkt liste geldiyse
        elif isinstance(results, dict) and 'items' in results:
            items = results['items']  # API response içinden items'ı al
        else:
            items = []

        for item in items:
            cur.execute("""
                INSERT INTO search_results 
                (search_id, title, link, display_link, formatted_url, 
                html_formatted_url, snippet, html_snippet, html_title, 
                kind, pagemap)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                search_id,
                item.get('title'),
                item.get('link'),
                item.get('displayLink'),
                item.get('formattedUrl'),
                item.get('htmlFormattedUrl'),
                item.get('snippet'),
                item.get('htmlSnippet'),
                item.get('htmlTitle'),
                item.get('kind'),
                Json(item.get('pagemap', {}))
            ))
        
        conn.commit()
        return search_id
        
    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close() 