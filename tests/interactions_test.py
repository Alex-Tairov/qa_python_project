from pages.interactions_page import DroppablePage

class TestDroppablePage:
    def test_simple_droppable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        text = droppable_page.drop_simple()
        assert text == 'Dropped!', "the elements has not been dropped"

    def test_accept_droppable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        not_accept, accept = droppable_page.drop_accept()
        assert not_accept == 'Drop here', "the dropped element has been accepted"
        assert accept == 'Dropped!', "the dropped element has not been accepted"

    def test_revert_draggable_droppable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open()
        will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will')
        not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will')
        assert will_after_move != will_after_revert, 'the elements has not reverted'
        assert not_will_after_move == not_will_after_revert, 'the elements has  reverted'