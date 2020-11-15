from lxml.html import clean
from typing import Any, Optional

_logger: Any
tags_to_kill: Any
tags_to_remove: Any
allowed_tags: Any
safe_attrs: Any

class _Cleaner(clean.Cleaner):
    _style_re: Any = ...
    _style_whitelist: Any = ...
    strip_classes: bool = ...
    sanitize_style: bool = ...
    def __call__(self, doc: Any) -> None: ...
    def tag_quote(self, el: Any): ...
    def strip_class(self, el: Any) -> None: ...
    def parse_style(self, el: Any) -> None: ...

def html_sanitize(src: Any, silent: bool = ..., sanitize_tags: bool = ..., sanitize_attributes: bool = ..., sanitize_style: bool = ..., sanitize_form: bool = ..., strip_style: bool = ..., strip_classes: bool = ...): ...

URL_REGEX: str
TEXT_URL_REGEX: str

def validate_url(url: Any): ...
def is_html_empty(html_content: Any): ...
def html_keep_url(text: Any): ...
def html2plaintext(html: Any, body_id: Optional[Any] = ..., encoding: str = ...): ...
def plaintext2html(text: Any, container_tag: bool = ...): ...
def append_content_to_html(html: Any, content: Any, plaintext: bool = ..., preserve: bool = ..., container_tag: bool = ...): ...

email_re: Any
single_email_re: Any
mail_header_msgid_re: Any
email_addr_escapes_re: Any

def generate_tracking_message_id(res_id: Any): ...
def email_send(email_from: Any, email_to: Any, subject: Any, body: Any, email_cc: Optional[Any] = ..., email_bcc: Optional[Any] = ..., reply_to: bool = ..., attachments: Optional[Any] = ..., message_id: Optional[Any] = ..., references: Optional[Any] = ..., openobject_id: bool = ..., debug: bool = ..., subtype: str = ..., headers: Optional[Any] = ..., smtp_server: Optional[Any] = ..., smtp_port: Optional[Any] = ..., ssl: bool = ..., smtp_user: Optional[Any] = ..., smtp_password: Optional[Any] = ..., cr: Optional[Any] = ..., uid: Optional[Any] = ...): ...
def email_split_tuples(text: Any): ...
def email_split(text: Any): ...
def email_split_and_format(text: Any): ...
def email_normalize(text: Any): ...
def email_escape_char(email_address: Any): ...
def decode_message_header(message: Any, header: Any, separator: str = ...): ...
def formataddr(pair: Any, charset: str = ...): ...