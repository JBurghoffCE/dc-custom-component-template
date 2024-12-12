from typing import List

from haystack import component


@component
class PostprocessingInvalidityComponent:
    @component.output_types(valid_query=str, invalid_query=str)
    def run(self, query: str, replies: List[str]):
        if replies[0] == "valid":
            return {"valid_query": query}
        else:
            return {"invalid_query": query}
