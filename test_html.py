from bs4 import BeautifulSoup

def test_html_content():
    with open("index.html", "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")
    
    assert soup.title.string == "Site Estático", "O título do HTML está incorreto!"
    assert soup.h1.string == "Bem-vindo ao meu site estático!", "O H1 está incorreto!"
    assert soup.p.string == "Este site foi implantado via AWS CodePipeline.", "O parágrafo está incorreto!"
