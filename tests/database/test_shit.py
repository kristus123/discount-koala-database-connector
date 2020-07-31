from discountkoala.database import DiscountKoalaDatabase



def test_sht():
	discountKoalaDatabase = DiscountKoalaDatabase("sqlite://")

	assert discountKoalaDatabase.session != None