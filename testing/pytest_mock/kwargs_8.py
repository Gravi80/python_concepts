# Allows you to configure your mock
from mock import patch


class Foo:
    def bar(self):
        pass


def test_kwargs():
    with patch('kwargs_8.Foo', attribute1='Some attr') as mock_foo:
        assert mock_foo.attribute1 == 'Some attr'


def test_kwargs_2():
    with patch('kwargs_8.Foo', **{'method1.return_value': 'Method1',
                                  'attribute1': 'Attribute1'}) as mock_foo:
        assert mock_foo.method1() == 'Method1'
        assert mock_foo.attribute1 == 'Attribute1'
