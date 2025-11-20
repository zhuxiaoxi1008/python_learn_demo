from format_name import format_name as fn

def test_format_name():
    ''' 测试函数 '''
    format_name = fn('janis', 'joplin')
    assert format_name == 'Janis Joplin'

test_format_name()