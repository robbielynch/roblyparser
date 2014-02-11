import re
__author__ = 'robbie'


class HTMLObject(object):
    """
    Class that holds the
    """

    title = ""
    description = ""
    keywords = []
    links = []
    images = []
    body_html = []
    body = ""
    robots_index = True

    def __init__(self):
        pass

    def tokens_to_html_object(self, tokens):
        for index, token in enumerate(tokens):
            #title
            if token.startswith("<title>"):
                self.title = tokens[index + 1]
            elif token.startswith("<body"):
                #Get body html
                body_html_tokens = []
                for t in tokens[index:]:
                    if t.startswith("</body>"):
                        break;
                    if not t.startswith("<body"):
                        body_html_tokens.append(t)
                #Get body content
                self.body_html = body_html_tokens
                self.body = self.get_body_content_as_string_from_body_tokens(body_html_tokens)
            elif token.startswith('<a '):
                #get links
                self.links.append(self.get_link_from_a_href_token(token))
            elif token.startswith('<img '):
                #get links
                self.images.append(self.get_link_from_img_src_token(token))



            #elif token.startswith('<meta name="description"') or token.startswith("<meta name='description'"):
            #    #description
            #    self.description = self.extract_description(token)

    def get_link_from_a_href_token(self, token):
        match = re.search(r'href=[\'"]?([^\'" >]+)', token)
        if match:
            link = match.group(0)
            return link[6:]
        else:
            return ""


    def get_body_content_as_string_from_body_tokens(self, body_tokens):
        if body_tokens:
            content_tokens = []
            for t in body_tokens:
                if not t.startswith('<'):
                    content_tokens.append(t)
            if content_tokens:
                body_content = ' '.join(content_tokens)
                return body_content
        return ""

    def get_link_from_img_src_token(self, token):
        match = re.search(r'src=[\'"]?([^\'" >]+)', token)
        if match:
            link = match.group(0)
            return link[5:]
        else:
            return ""



