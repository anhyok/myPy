# stub
from unittest.mock import MagicMock

def test_stub():
    # 스텁 생성
    stub = MagicMock()
    # 스텁의 add 메서드가 무조건 5를 반환하도록 설정
    stub.add.return_value = 5
    stub.mul.return_value = 10
    result = stub.add(2, 3)
    result2 = stub.mul(2, 5)
    # 스텁의 add 메서드가 5를 반환했기 때문에, result는 항상 5입니다.
    assert result == 5
    assert result2 == 10


# mock
from unittest.mock import Mock

def test_mock():
    # 모의 객체 생성
    mock = Mock()
    mock.add(2, 3)

    # mock의 add 메서드가 한 번 호출되었는지 검증
    mock.add.assert_called_once()
    # mock의 add 메서드가 (2, 3)으로 호출되었는지 검증
    mock.add.assert_called_with(2, 3)


test_stub()
test_mock()
