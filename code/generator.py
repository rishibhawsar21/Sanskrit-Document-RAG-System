def generate_answer(query, context):
    """
    Lightweight generator:
    Returns the most relevant retrieved Sanskrit context
    as the final answer (extractive RAG).
    """

    if not context.strip():
        return "उत्तरः न उपलब्धः।"

    # Simple post-processing
    lines = context.split("\n")
    answer = lines[0].strip()

    return answer
