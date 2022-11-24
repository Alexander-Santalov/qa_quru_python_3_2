from selene import be, have


def test_google_positive(app):
    app.element("[name='q']").should(be.blank).type("selene").press_enter()
    app.element("[id='search']").should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_google_negative(app):
    app.element("[name='q']").clear().type("weqweqwxqdscfbjvghwjernfvwekndflkw").press_enter()
    app.element("div.card-section").should(
        have.text('По запросу weqweqwxqdscfbjvghwjernfvwekndflkw ничего не найдено.'))
