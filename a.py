from gpt_index import GPTSimpleVectorIndex, download_loader


SimpleDirectoryReader = download_loader("SimpleDirectoryReader")

loader = SimpleDirectoryReader('./data', recursive=True, exclude_hidden=True)
documents = loader.load_data()
index = GPTSimpleVectorIndex(documents)
result = index.query('')
print(result)
