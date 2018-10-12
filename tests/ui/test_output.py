from python_tictactoe.ui.output import Output

class TestOutput(object):

    def test_that_it_prints_the_output(self, capsys):
        output = Output()
        output.display("test")

        captured = capsys.readouterr()
        assert captured.out == "test\n"