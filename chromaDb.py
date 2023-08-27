import chromadb
import PyPDF2
from chromadb.config import Settings
from langchain.text_splitter import CharacterTextSplitter


class chromaDbFunctions:

    def __init__(self):
        self.client = chromadb.Client(Settings(chroma_api_impl="rest",
                                             chroma_server_host="localhost",
                                             chroma_server_http_port="8000"
                                             ))

    def uploadPdf(self, file, fileName):
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        text_list = []
        pdfReader = PyPDF2.PdfReader(file)
        # print("Page Number:", len(pdfReader.pages))
        for i in range(len(pdfReader.pages)):
            pageObj = pdfReader.pages[i]
            text = pageObj.extract_text()
            pageObj.clear()
            text_list.extend(text_splitter.split_text(text))

        # document_iterable = self.list_to_iterable_document(text_list)
        # text_splitter.split_text(text_list)
        # coachbarDocTexts = text_splitter.split_documents(document_iterable)
        #
        # coachbarDocdDb = Chroma.from_documents(coachbarDocTexts, embeddings)


        collection = self.client.get_collection("test")
        metas = [{"source": fileName} for i in range(1, len(text_list) + 1)]
        ids = [str(i) for i in range(1, len(text_list) + 1)]
        collection.add(documents=text_list, metadatas=metas, ids=ids)

    def peek(self):
        collection = self.client.get_collection("test")
        return collection.peek()


    def list_to_iterable_document(self, string_list):
        def document_generator():
            for line in string_list:
                yield line
        return document_generator()
