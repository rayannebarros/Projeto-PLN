# Load Packages
import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

document1 = """Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning.In its application across business problems, machine learning is also referred to as predictive analytics."""

parser = PlaintextParser.from_string(document1, Tokenizer("english"))

# Using LexRank
summarizer = LexRankSummarizer()
# Summarize the document with 2 sentences
summary = summarizer(parser.document, 2)

# for sentence in summary:
#     print(sentence)

from sumy.summarizers.luhn import LuhnSummarizer

summarizer_luhn = LuhnSummarizer()
summary_1 = summarizer_luhn(parser.document, 2)

# for sentence in summary_1:
#     print(sentence)

from sumy.summarizers.lsa import LsaSummarizer

summarizer_lsa = LsaSummarizer()
summary_2 = summarizer_lsa(parser.document, 2)

for sentence in summary_2:
    print(sentence)

# Ler pdf e extrair texto
# f = open(r'C:\Users\micas\Desktop\Faculdade\Matérias\RHT\Sentidos e Significados do Trabalho - Resumo a ser feito sobre o artigo.pdf', 'rb')
# pdf = PyPDF2.PdfFileReader(f)
# spg = pdf.getPage(1).extractText()
# f.close()
# print(luhn(spg))
