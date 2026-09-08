# -*- coding: utf-8 -*-
# 小龙智脑 (XiaoLong Brain) — 项目生成脚本
# 作者 / 版权人: 小龙 (XiaoLong)
# 本脚本用于一次性生成「小龙智脑」全部原创源码文件，可重复运行。

import os

HEADER = (
    "# -*- coding: utf-8 -*-\n"
    "# 小龙智脑 (XiaoLong Brain) - 全新原创项目\n"
    "# 作者 / 版权人: 小龙 (XiaoLong)\n"
    "# License: MIT。本项目所有代码均为原创，保留署名即可自由使用。\n"
)

FILES = {}

FILES["LICENSE"] = """MIT License

Copyright (c) 2026 小龙 (XiaoLong)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

FILES["README.md"] = """# 小龙智脑 (XiaoLong Brain)

> 由 **小龙 (XiaoLong)** 全新原创的轻量级 Python AI 工具包：智能体(Agent)、记忆、工具调用、检索增强生成(RAG)、嵌入与向量检索，全部用标准库实现，**零第三方依赖**。

## 特性

- **零依赖**：仅用 Python 标准库，开箱即用。
- **智能体框架**：`Agent` 支持多轮记忆与工具调用（协议 `[TOOL:name(k=v)]`）。
- **RAG 检索**：`Retriever` + `InMemoryVectorStore` + `HashEmbeddings`，几行即可检索。
- **可插拔 LLM**：内置 `MockLLM`（离线演示），并支持任意 OpenAI 兼容接口。
- **评估模块**：`exact_match` / `token_f1` / `rouge_l` 开箱即用。
- **CLI 与 HTTP 服务**：`xiaolong` 命令行 + 内置 HTTP 服务。

## 目录结构

```
xiaolong_ai/
  version.py          版本与作者信息
  core/               核心：config / tokenizer / prompt / memory / llm
                      embeddings / vectorstore / document / retriever / tool / agent
  tools/              内置工具：calculator / datetime / file / python_exec
  utils/              logging / text / cache
  eval/               metrics / harness
  examples/           示例：basic_agent / rag_demo
  cli.py              命令行入口
  server.py           内置 HTTP 服务
tests/                单元测试
```

## 快速开始

```bash
# 对话（使用本地 Mock 模型）
python -m xiaolong_ai.cli chat

# 对文档做检索
python -m xiaolong_ai.cli rag --file doc.txt --query "小龙智脑是什么" --top_k 3

# 启动 HTTP 服务
python -m xiaolong_ai.server
```

## 接入真实大模型

`OpenAICompatibleLLM` 兼容任意 OpenAI 风格接口（含本地推理服务）：

```python
from xiaolong_ai.core.llm import OpenAICompatibleLLM
from xiaolong_ai.core.agent import Agent

llm = OpenAICompatibleLLM(api_base="http://localhost:8000/v1", api_key="EMPTY", model="local")
agent = Agent(llm=llm, system_prompt="你是小龙智脑。")
print(agent.run("帮我算 12 * 8"))
```

## 版权说明

- 本项目（`xiaolong-ai/`）下所有代码均为 **小龙 (XiaoLong)** 原创，采用 MIT 协议。
- 同仓库内的 `reference/` 目录为从 GitHub 下载的**第三方开源项目**（如 HuggingFace Transformers），其版权归原作者所有，仅作本地学习参考，请遵守其各自 LICENSE。

作者：小龙 (XiaoLong)  |  License：MIT
"""

FILES["pyproject.toml"] = """[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "xiaolong-ai"
version = "0.1.0"
description = "小龙智脑 - 由小龙打造的轻量级 Python AI 工具包（Agent / RAG / 工具调用，零依赖）"
readme = "README.md"
requires-python = ">=3.8"
license = { text = "MIT" }
authors = [{ name = "小龙 (XiaoLong)" }]
keywords = ["ai", "agent", "rag", "llm", "xiaolong"]

[project.scripts]
xiaolong = "xiaolong_ai.cli:main"

[tool.setuptools]
packages = ["xiaolong_ai", "xiaolong_ai.core", "xiaolong_ai.tools", "xiaolong_ai.utils", "xiaolong_ai.eval", "xiaolong_ai.examples"]
"""

FILES[".gitignore"] = """# 小龙智脑 忽略规则
__pycache__/
*.py[cod]
*.egg-info/
build/
dist/
.xiaolong_cache.json
xiaolong_workspace/
.pytest_cache/
*.log
"""

FILES["requirements.txt"] = """# 小龙智脑 零第三方依赖，仅需 Python 3.8+ 标准库。
# 如需接入真实大模型，仅需能访问对应 HTTP 接口，无需额外安装包。
"""

FILES["xiaolong_ai/__init__.py"] = """from xiaolong_ai.version import __version__, __author__, __license__

__all__ = ["__version__", "__author__", "__license__"]
"""

FILES["xiaolong_ai/version.py"] = """__version__ = "0.1.0"
__author__ = "小龙 (XiaoLong)"
__license__ = "MIT"
"""

FILES["xiaolong_ai/core/__init__.py"] = """from xiaolong_ai.core.config import Config
from xiaolong_ai.core.memory import ConversationMemory
from xiaolong_ai.core.llm import LLM, MockLLM, OpenAICompatibleLLM
from xiaolong_ai.core.agent import Agent
from xiaolong_ai.core.tool import Tool, ToolRegistry, tool, get_default_registry
from xiaolong_ai.core.embeddings import Embeddings, HashEmbeddings
from xiaolong_ai.core.vectorstore import InMemoryVectorStore
from xiaolong_ai.core.document import Document, TextLoader, chunk_text
from xiaolong_ai.core.retriever import Retriever

__all__ = [
    "Config", "ConversationMemory", "LLM", "MockLLM", "OpenAICompatibleLLM",
    "Agent", "Tool", "ToolRegistry", "tool", "get_default_registry",
    "Embeddings", "HashEmbeddings", "InMemoryVectorStore",
    "Document", "TextLoader", "chunk_text", "Retriever",
]
"""

FILES["xiaolong_ai/core/config.py"] = """import json
import os
from dataclasses import dataclass, field, asdict


@dataclass
class Config:
    # 模型名称，默认使用本地 Mock
    model_name: str = "mock"
    # OpenAI 兼容接口地址
    api_base: str = ""
    api_key: str = ""
    temperature: float = 0.7
    max_tokens: int = 1024
    # 工作区目录（文件工具默认落盘位置）
    workspace: str = "./xiaolong_workspace"
    # 额外自定义配置
    extra: dict = field(default_factory=dict)

    @classmethod
    def load(cls, path):
        if not os.path.exists(path):
            return cls()
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        known = {k: v for k, v in data.items() if k in cls.__dataclass_fields__}
        cfg = cls(**known)
        cfg.extra = {k: v for k, v in data.items() if k not in cls.__dataclass_fields__}
        return cfg

    def save(self, path):
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(asdict(self), f, ensure_ascii=False, indent=2)

    def get(self, key, default=None):
        return self.extra.get(key, default)
"""

FILES["xiaolong_ai/core/tokenizer.py"] = """import re

# 中日韩统一表意文字区间
_CJK = re.compile(r"[一-鿿]")


def tokenize(text):
    # 英文/数字按词切分，CJK 按字切分
    if not text:
        return []
    tokens = []
    for piece in re.split(r"\\s+", text):
        if not piece:
            continue
        non_cjk = _CJK.sub(" ", piece).strip()
        if non_cjk:
            tokens.extend(re.findall(r"[A-Za-z0-9]+|[^\\sA-Za-z0-9]", non_cjk))
        tokens.extend(_CJK.findall(piece))
    return tokens


def count_tokens(text):
    return len(tokenize(text))
"""

FILES["xiaolong_ai/core/prompt.py"] = """import re


class PromptTemplate:
    def __init__(self, template):
        self.template = template
        self.vars = set(re.findall(r"\\{(\\w+)\\}", template))

    def format(self, **kwargs):
        missing = self.vars - set(kwargs.keys())
        if missing:
            raise KeyError("Missing template variables: %s" % ", ".join(sorted(missing)))
        return self.template.format(**kwargs)

    def render(self, context):
        return self.format(**context)


def system_prompt(role="助手"):
    return "你是%s，由小龙(XiaoLong)打造的智能助手，回答准确、简洁、有用。" % role


def user_prompt(text):
    return text
"""

FILES["xiaolong_ai/core/memory.py"] = """from dataclasses import dataclass, field


@dataclass
class Message:
    role: str
    content: str
    metadata: dict = field(default_factory=dict)

    def to_dict(self):
        return {"role": self.role, "content": self.content, "metadata": self.metadata}


class ConversationMemory:
    def __init__(self, max_turns=None):
        self.max_turns = max_turns
        self.messages = []

    def add(self, role, content, metadata=None):
        self.messages.append(Message(role, content, metadata or {}))
        self._trim()

    def _trim(self):
        if self.max_turns and len(self.messages) > self.max_turns * 2:
            self.messages = self.messages[-self.max_turns * 2:]

    def history(self, as_text=False):
        if as_text:
            return "\\n".join("[%s]: %s" % (m.role, m.content) for m in self.messages)
        return [m.to_dict() for m in self.messages]

    def clear(self):
        self.messages = []

    def __len__(self):
        return len(self.messages)
"""

FILES["xiaolong_ai/core/llm.py"] = """import json
import urllib.request
import urllib.error


class LLM:
    # 大模型抽象基类
    def complete(self, prompt, **kwargs):
        raise NotImplementedError

    def chat(self, messages, **kwargs):
        raise NotImplementedError


class MockLLM(LLM):
    # 离线演示用本地模型，不联网
    def __init__(self, mode="echo"):
        self.mode = mode

    def complete(self, prompt, **kwargs):
        if self.mode == "echo":
            return "【小龙智脑-Mock】收到指令：%s" % prompt
        return "【小龙智脑-Mock】我是一个用于演示的本地模型，暂未接入真实大模型。"

    def chat(self, messages, **kwargs):
        last = messages[-1]["content"] if messages else ""
        return self.complete(last, **kwargs)


class OpenAICompatibleLLM(LLM):
    # 兼容任意 OpenAI 风格 /v1/chat/completions 接口
    def __init__(self, api_base, api_key, model="gpt-3.5-turbo", timeout=30):
        self.api_base = api_base.rstrip("/")
        self.api_key = api_key
        self.model = model
        self.timeout = timeout

    def chat(self, messages, **kwargs):
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": kwargs.get("temperature", 0.7),
            "max_tokens": kwargs.get("max_tokens", 1024),
        }
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            self.api_base + "/chat/completions",
            data=data,
            headers={"Content-Type": "application/json",
                     "Authorization": "Bearer %s" % self.api_key},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            result = json.loads(resp.read().decode("utf-8"))
        return result["choices"][0]["message"]["content"]

    def complete(self, prompt, **kwargs):
        return self.chat([{"role": "user", "content": prompt}], **kwargs)
"""

FILES["xiaolong_ai/core/embeddings.py"] = """import math
import re


class Embeddings:
    def embed(self, text):
        raise NotImplementedError

    def embed_batch(self, texts):
        return [self.embed(t) for t in texts]


class HashEmbeddings(Embeddings):
    # 基于词哈希的确定性嵌入，无需任何模型文件，适合演示与基线
    def __init__(self, dim=256):
        self.dim = dim

    def embed(self, text):
        vec = [0.0] * self.dim
        tokens = re.findall(r"[a-z0-9]+|[一-鿿]", (text or "").lower())
        for tok in tokens:
            h = hash(tok) % self.dim
            vec[h] += 1.0
        norm = math.sqrt(sum(v * v for v in vec))
        if norm > 0:
            vec = [v / norm for v in vec]
        return vec
"""

FILES["xiaolong_ai/core/vectorstore.py"] = """import math


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


class InMemoryVectorStore:
    def __init__(self, embedding_fn):
        self.embedding_fn = embedding_fn
        self.items = []

    def add(self, text, metadata=None):
        vec = self.embedding_fn.embed(text)
        self.items.append({"text": text, "vec": vec, "metadata": metadata or {}})

    def add_documents(self, docs):
        for d in docs:
            self.add(d["text"], d.get("metadata"))

    def search(self, query, top_k=3):
        qv = self.embedding_fn.embed(query)
        scored = [(cosine(qv, it["vec"]), it) for it in self.items]
        scored.sort(key=lambda x: x[0], reverse=True)
        return [{"score": s, "text": it["text"], "metadata": it["metadata"]}
                for s, it in scored[:top_k]]
"""

FILES["xiaolong_ai/core/document.py"] = """import re


class Document:
    def __init__(self, text, metadata=None):
        self.text = text
        self.metadata = metadata or {}

    def __repr__(self):
        return "Document(len=%d, meta=%s)" % (len(self.text), self.metadata)


class TextLoader:
    def load(self, path):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        return Document(text, {"source": path})

    def load_text(self, text, metadata=None):
        return Document(text, metadata or {})


def chunk_text(text, chunk_size=200, overlap=40):
    # 按句子切分，并保留 overlap 重叠，避免句子被截断
    if chunk_size <= overlap:
        overlap = 0
    sentences = re.split(r"(?<=[。！？.!?])\\s*", text)
    chunks = []
    buf = ""
    for sent in sentences:
        if not sent.strip():
            continue
        if len(buf) + len(sent) > chunk_size and buf:
            chunks.append(buf.strip())
            buf = buf[-overlap:] + sent
        else:
            buf += sent
    if buf.strip():
        chunks.append(buf.strip())
    return chunks
"""

FILES["xiaolong_ai/core/retriever.py"] = """from xiaolong_ai.core.embeddings import HashEmbeddings
from xiaolong_ai.core.vectorstore import InMemoryVectorStore
from xiaolong_ai.core.document import chunk_text


class Retriever:
    # 检索增强（RAG）核心：索引文档 + 语义检索
    def __init__(self, embedding_fn=None, chunk_size=200, overlap=40):
        self.embedding_fn = embedding_fn or HashEmbeddings()
        self.store = InMemoryVectorStore(self.embedding_fn)
        self.chunk_size = chunk_size
        self.overlap = overlap

    def index(self, text, source="doc"):
        for i, c in enumerate(chunk_text(text, self.chunk_size, self.overlap)):
            self.store.add(c, {"source": source, "chunk": i})

    def retrieve(self, query, top_k=3):
        return self.store.search(query, top_k)
"""

FILES["xiaolong_ai/core/tool.py"] = """import inspect


class Tool:
    def __init__(self, name, func, description=""):
        self.name = name
        self.func = func
        self.description = description or (func.__doc__ or "").strip()

    def run(self, **kwargs):
        return self.func(**kwargs)

    def spec(self):
        return {"name": self.name, "description": self.description,
                "parameters": list(inspect.signature(self.func).parameters)}


class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, tool):
        self.tools[tool.name] = tool
        return tool

    def register_fn(self, name, func, description=""):
        return self.register(Tool(name, func, description))

    def get(self, name):
        return self.tools.get(name)

    def list(self):
        return [t.spec() for t in self.tools.values()]

    def call(self, name, **kwargs):
        tool = self.tools.get(name)
        if not tool:
            raise KeyError("Unknown tool: %s" % name)
        return tool.run(**kwargs)


# 全局默认工具注册表
_default_registry = ToolRegistry()


def tool(name=None, description=""):
    # 装饰器：把函数注册为工具
    def deco(func):
        tname = name or func.__name__
        _default_registry.register(Tool(tname, func, description))
        return func
    return deco


def get_default_registry():
    return _default_registry
"""

FILES["xiaolong_ai/core/agent.py"] = """import re
from xiaolong_ai.core.memory import ConversationMemory
from xiaolong_ai.core.tool import get_default_registry


# 工具调用协议： [TOOL:name(key="value", key2="value2")]
_TOOL_CALL = re.compile(r"\\[TOOL:(\\w+)\\((.*?)\\)\\]")


def _parse_args(argstr):
    args = {}
    if not argstr.strip():
        return args
    for part in argstr.split(","):
        if "=" in part:
            k, v = part.split("=", 1)
            args[k.strip()] = v.strip().strip("\\"'")
    return args


class Agent:
    # 多轮记忆 + 工具调用的轻量智能体
    def __init__(self, llm=None, system_prompt="你是小龙智脑助手。",
                 registry=None, max_steps=5):
        self.llm = llm
        self.system_prompt = system_prompt
        self.registry = registry or get_default_registry()
        self.memory = ConversationMemory()
        self.max_steps = max_steps

    def _build_messages(self, user_input):
        msgs = [{"role": "system", "content": self.system_prompt}]
        msgs += self.memory.history()
        tools_desc = "; ".join("%s(%s)" % (t["name"], ",".join(t["parameters"]))
                               for t in self.registry.list()) or "无"
        msgs.append({"role": "system", "content": "可用工具: " + tools_desc})
        msgs.append({"role": "user", "content": user_input})
        return msgs

    def run(self, user_input):
        if not self.llm:
            raise RuntimeError("Agent 需要一个 LLM 实例")
        self.memory.add("user", user_input)
        for step in range(self.max_steps):
            msgs = self._build_messages(user_input if step == 0 else "")
            reply = self.llm.chat(msgs)
            match = _TOOL_CALL.search(reply)
            if match:
                name = match.group(1)
                args = _parse_args(match.group(2))
                try:
                    result = self.registry.call(name, **args)
                except Exception as e:
                    result = "工具执行出错: %s" % e
                self.memory.add("assistant", reply)
                self.memory.add("tool", "工具 %s 返回: %s" % (name, result))
                continue
            self.memory.add("assistant", reply)
            return reply
        return "（已达到最大步数，未能完成）"
"""

FILES["xiaolong_ai/tools/__init__.py"] = """# 导入子模块以触发工具注册
from xiaolong_ai.tools import calculator, datetime_tool, file_tool, python_exec

__all__ = ["calculator", "datetime_tool", "file_tool", "python_exec"]
"""

FILES["xiaolong_ai/tools/calculator.py"] = """from xiaolong_ai.core.tool import tool

_ALLOWED = set("0123456789+-*/().% ")


@tool(name="calculator", description='计算数学表达式，如 calculator(expression="1+2*3")')
def calculator(expression):
    # 仅允许基本四则运算字符，禁用内建函数，保证安全
    if not expression or set(expression) - _ALLOWED:
        raise ValueError("仅支持基本四则运算")
    return str(eval(expression, {"__builtins__": {}}, {}))
"""

FILES["xiaolong_ai/tools/datetime_tool.py"] = """from datetime import datetime
from xiaolong_ai.core.tool import tool


@tool(name="now", description="返回当前日期时间，如 now()")
def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
"""

FILES["xiaolong_ai/tools/file_tool.py"] = """import os
from xiaolong_ai.core.tool import tool

_BASE = os.path.abspath("./xiaolong_workspace")


@tool(name="read_file", description='读取工作区文件，如 read_file(path="a.txt")')
def read_file(path):
    full = os.path.join(_BASE, path)
    with open(full, "r", encoding="utf-8") as f:
        return f.read()


@tool(name="write_file", description='写入工作区文件，如 write_file(path="a.txt", content="hi")')
def write_file(path, content):
    full = os.path.join(_BASE, path)
    os.makedirs(os.path.dirname(os.path.abspath(full)), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return "已写入 %d 字符" % len(content)
"""

FILES["xiaolong_ai/tools/python_exec.py"] = """from xiaolong_ai.core.tool import tool


@tool(name="python_exec", description='在受限环境执行 Python 代码片段，如 python_exec(code="print(1+1)")')
def python_exec(code):
    # 演示用途：捕获 print 输出，异常安全返回
    buffer = []

    def _print(*a, **k):
        buffer.append(" ".join(str(x) for x in a))

    env = {"print": _print, "__builtins__": __builtins__}
    try:
        exec(code, env)
    except Exception as e:
        return "错误: %s" % e
    return "\\n".join(buffer) if buffer else "执行成功（无输出）"
"""

FILES["xiaolong_ai/utils/__init__.py"] = """from xiaolong_ai.utils import logging, text, cache

__all__ = ["logging", "text", "cache"]
"""

FILES["xiaolong_ai/utils/logging.py"] = """import sys
import time


class Logger:
    def __init__(self, name="xiaolong", level="INFO"):
        self.name = name
        self.level = level

    def _log(self, level, msg):
        ts = time.strftime("%H:%M:%S")
        print("[%s][%s][%s] %s" % (ts, level, self.name, msg), file=sys.stderr, flush=True)

    def info(self, msg):
        self._log("INFO", msg)

    def warn(self, msg):
        self._log("WARN", msg)

    def error(self, msg):
        self._log("ERROR", msg)


logger = Logger()
"""

FILES["xiaolong_ai/utils/text.py"] = """def truncate(text, max_len=100, suffix="..."):
    if len(text) <= max_len:
        return text
    return text[:max_len - len(suffix)] + suffix


def normalize_whitespace(text):
    return " ".join(text.split())
"""

FILES["xiaolong_ai/utils/cache.py"] = """import json
import os
import time
import hashlib


class JsonCache:
    def __init__(self, path="./xiaolong_cache.json", ttl=3600):
        self.path = path
        self.ttl = ttl
        self.store = self._load()

    def _load(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.store, f, ensure_ascii=False)

    def get(self, key):
        item = self.store.get(key)
        if not item:
            return None
        if self.ttl > 0 and time.time() - item["t"] > self.ttl:
            return None
        return item["v"]

    def set(self, key, value):
        self.store[key] = {"t": time.time(), "v": value}
        self._save()

    @staticmethod
    def key(*parts):
        return hashlib.md5("|".join(str(p) for p in parts).encode("utf-8")).hexdigest()
"""

FILES["xiaolong_ai/cli.py"] = """import argparse
from xiaolong_ai.core.llm import MockLLM
from xiaolong_ai.core.agent import Agent
from xiaolong_ai.core.retriever import Retriever
from xiaolong_ai.tools import calculator, datetime_tool, file_tool, python_exec


def cmd_chat(args):
    agent = Agent(llm=MockLLM(), system_prompt="你是小龙智脑，由小龙打造。")
    print("小龙智脑已就绪，输入 exit 退出。")
    while True:
        try:
            q = input("你> ")
        except EOFError:
            break
        if q.strip().lower() in ("exit", "quit"):
            break
        print("小龙> " + agent.run(q))


def cmd_rag(args):
    retriever = Retriever()
    with open(args.file, "r", encoding="utf-8") as f:
        retriever.index(f.read(), source=args.file)
    for r in retriever.retrieve(args.query, top_k=args.top_k):
        print("[%.3f] %s" % (r["score"], r["text"]))


def build_parser():
    p = argparse.ArgumentParser(prog="xiaolong", description="小龙智脑 CLI")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("chat", help="进入对话模式")
    rag = sub.add_parser("rag", help="对文档做检索")
    rag.add_argument("--file", required=True)
    rag.add_argument("--query", required=True)
    rag.add_argument("--top_k", type=int, default=3)
    return p


def main():
    parser = build_parser()
    args = parser.parse_args()
    if args.cmd == "chat":
        cmd_chat(args)
    elif args.cmd == "rag":
        cmd_rag(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
"""

FILES["xiaolong_ai/server.py"] = """import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from xiaolong_ai.core.llm import MockLLM
from xiaolong_ai.core.agent import Agent


class Handler(BaseHTTPRequestHandler):
    agent = Agent(llm=MockLLM())

    def _send(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length) if length else b"{}"
        try:
            data = json.loads(raw.decode("utf-8") or "{}")
        except Exception:
            data = {}
        reply = self.agent.run(data.get("message", ""))
        self._send({"reply": reply})

    def log_message(self, *a):
        pass


def serve(port=8000):
    print("小龙智脑服务已启动: http://127.0.0.1:%d" % port)
    HTTPServer(("127.0.0.1", port), Handler).serve_forever()


if __name__ == "__main__":
    serve()
"""

FILES["xiaolong_ai/eval/__init__.py"] = """from xiaolong_ai.eval import metrics, harness

__all__ = ["metrics", "harness"]
"""

FILES["xiaolong_ai/eval/metrics.py"] = """import re


def normalize(text):
    return " ".join(re.findall(r"[a-z0-9一-鿿]+", (text or "").lower()))


def exact_match(pred, gold):
    return normalize(pred) == normalize(gold)


def token_f1(pred, gold):
    p = normalize(pred).split()
    g = normalize(gold).split()
    if not p and not g:
        return 1.0
    common = set(p) & set(g)
    if not common:
        return 0.0
    prec = len(common) / len(p)
    rec = len(common) / len(g)
    return 2 * prec * rec / (prec + rec)


def rouge_l(pred, gold):
    p = normalize(pred).split()
    g = normalize(gold).split()
    if not g:
        return 1.0 if not p else 0.0
    m, n = len(p), len(g)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[i - 1] == g[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs = dp[m][n]
    rec = lcs / len(g)
    prec = lcs / len(p) if p else 0.0
    if prec + rec == 0:
        return 0.0
    return 2 * prec * rec / (prec + rec)


def evaluate(pred, gold):
    return {
        "exact_match": exact_match(pred, gold),
        "token_f1": token_f1(pred, gold),
        "rouge_l": rouge_l(pred, gold),
    }
"""

FILES["xiaolong_ai/eval/harness.py"] = """from xiaolong_ai.eval.metrics import evaluate


def run_dataset(dataset):
    # dataset: list of {"pred": ..., "gold": ...}
    total = {"exact_match": 0.0, "token_f1": 0.0, "rouge_l": 0.0}
    n = 0
    for item in dataset:
        r = evaluate(item.get("pred", ""), item.get("gold", ""))
        for k in total:
            total[k] += float(r[k])
        n += 1
    if n == 0:
        return total
    return {k: v / n for k, v in total.items()}
"""

FILES["xiaolong_ai/examples/__init__.py"] = """# 小龙智脑 示例模块
"""

FILES["xiaolong_ai/examples/basic_agent.py"] = """from xiaolong_ai.core.llm import MockLLM
from xiaolong_ai.core.agent import Agent
from xiaolong_ai.tools import calculator


def main():
    agent = Agent(llm=MockLLM(), system_prompt="你是小龙智脑演示助手。")
    print(agent.run("你好，介绍一下你自己"))
    print("计算器:", calculator.calculator("1+2*3"))


if __name__ == "__main__":
    main()
"""

FILES["xiaolong_ai/examples/rag_demo.py"] = """from xiaolong_ai.core.retriever import Retriever


def main():
    text = ("小龙智脑是 XiaoLong 打造的开源 AI 工具包。"
            "它支持记忆、工具调用与检索增强生成。"
            "项目完全原创，采用 MIT 协议发布。")
    retriever = Retriever()
    retriever.index(text, source="demo")
    for r in retriever.retrieve("小龙智脑是什么", top_k=2):
        print("[%.3f] %s" % (r["score"], r["text"]))


if __name__ == "__main__":
    main()
"""

FILES["tests/__init__.py"] = """# 小龙智脑 单元测试
"""

FILES["tests/test_core.py"] = """from xiaolong_ai.core.tokenizer import tokenize, count_tokens
from xiaolong_ai.core.memory import ConversationMemory
from xiaolong_ai.core.prompt import PromptTemplate
from xiaolong_ai.core.embeddings import HashEmbeddings
from xiaolong_ai.core.vectorstore import InMemoryVectorStore
from xiaolong_ai.core.document import chunk_text
from xiaolong_ai.core.retriever import Retriever


def test_tokenize():
    toks = tokenize("Hello 世界 123")
    assert "Hello" in toks and "世" in toks and "123" in toks


def test_count_tokens():
    assert count_tokens("a b c") == 3


def test_memory():
    m = ConversationMemory()
    m.add("user", "hi")
    m.add("assistant", "hello")
    assert len(m) == 2


def test_prompt():
    t = PromptTemplate("你好 {name}")
    assert "小龙" in t.format(name="小龙")


def test_embeddings_and_store():
    emb = HashEmbeddings(dim=64)
    store = InMemoryVectorStore(emb)
    store.add("小龙 智脑 开源")
    store.add("苹果 水果 甜")
    res = store.search("小龙", top_k=1)
    assert "小龙" in res[0]["text"]


def test_chunk():
    chunks = chunk_text("句子一。句子二。句子三。", chunk_size=10, overlap=2)
    assert len(chunks) >= 1


def test_retriever():
    r = Retriever(chunk_size=50)
    r.index("小龙智脑支持 RAG 检索。", source="x")
    assert len(r.retrieve("RAG", top_k=1)) == 1
"""

FILES["tests/test_tools.py"] = """from xiaolong_ai.tools.calculator import calculator
from xiaolong_ai.tools.datetime_tool import now
from xiaolong_ai.core.tool import get_default_registry


def test_calculator():
    assert calculator("1+2*3") == "7"


def test_now():
    assert len(now()) >= 8


def test_registry():
    reg = get_default_registry()
    assert reg.get("calculator") is not None
    assert reg.get("now") is not None
"""


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    for rel, content in FILES.items():
        target = os.path.join(here, rel)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        if rel.endswith(".py"):
            content = HEADER + "\n" + content
        with open(target, "w", encoding="utf-8") as f:
            f.write(content)
        print("written:", rel)


if __name__ == "__main__":
    main()
