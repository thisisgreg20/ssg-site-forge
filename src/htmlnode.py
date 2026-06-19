class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None or not self.props:
            return ""
        return "".join(f' {key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        tag_props = self.props_to_html()
        tag_open = f"<{self.tag}{tag_props}>"
        tag_close = f"</{self.tag}>"
        tag_complete_string = f"{tag_open}{self.value}{tag_close}"
        return tag_complete_string
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"