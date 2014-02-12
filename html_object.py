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
            elif token.startswith('<meta'):
                #Get meta Keywords
                keywords = self.get_keywords_from_meta_tag(token)
                if keywords:
                    if 'keywords' in token:
                        self.keywords = keywords
                else:
                    #Check for meta description
                    if 'description' in token:
                        self.description = self.get_description_from_meta_tag(token)

                



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

    def get_keywords_from_meta_tag(self, token):
        keywords_string = ""
        keywords_list = []
        #keyword_regex = re.compile(r'<meta\sname=["\']keywords["\']\scontent=["\'](.*?)["\']\s/>')
        match = re.search(r'<meta[\s]*name=[\'"]keywords[\'"][\s]*content=[\'"]([\w, ]*)[\'"][. ]*[/>]*', token)

        try:
            if match:
                content_match = re.search(r'content=[\'"]([\w, ]*)[\'"][. ]*[/>]*', match.group(0))
                keywords_match = re.search(r'content=[\'"]([\w, ]*)[\'"]', content_match.group(0))
                keywords_string = keywords_match.group(0)[9:len(keywords_match.group(0))-1]

            if keywords_string:
                keywords_string = keywords_string.replace(",", " ")
                keywords_list = keywords_string.split()
        except Exception as e:
            print("[RoblyParser] error parsing keywords - {}".format(str(e)))
        return keywords_list

    def get_description_from_meta_tag(self, token):
        token = token.replace("\'", r"'")
        token = token.replace("\!", r"!")
        token = token.replace("\-", r"-")
        token = token.replace("\,", r",")
        description_string = ""
        match = re.search('<meta[\s]*name=[\'"]description[\'"][\s]*content=[\'"]([\w, \W]*)[\'"][. ]*[/>]*', token)

        try:
            if match:
                content_match = re.search(r'content=[\'"]([\w, \W\\]*)[\'"][. ]*[/>]*', match.group(0))
                desc_match = re.search(r'content=[\'"]([\w, \W\\]*)[\'"]', content_match.group(0))
                description_string = desc_match.group(0)[12:len(desc_match.group(0))-1]
                return description_string
        except Exception as e:
            print("[RoblyParser] error parsing keywords - {}".format(str(e)))
        return description_string


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


