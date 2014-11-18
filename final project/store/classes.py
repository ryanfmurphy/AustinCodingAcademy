import MySQLdb
import MySQLdb.cursors


class Database():
    def __init__(self):
        self.conn = MySQLdb.connect(host='acadb.cz0wsfs6bppg.us-west-2.rds.amazonaws.com',
                                    user='root', passwd='something', db='acadb', port=3306,
                                    cursorclass=MySQLdb.cursors.DictCursor)

        self.cur = self.conn.cursor()

    def get_results(self, query):
        """
        Get results from a given select query
        :param query: Which select query do you want to run
        :return: list of dictionaries
        """
        self.cur.execute(query)
        results = self.cur.fetchall()
        self.conn.commit()

        return results




class Product():
    def __init__(self):
        self.db = Database()

    def get_all_products(self):
        """
        Get all products from the database
        :return:
        """
        query = 'select * from product'
        return self.db.get_results(query)

    def get_product_by_id(self, product_id):
        """
        Get one product by id
        :param product_id: product.product_id from the product table
        :return: one product
        """
        query = 'select * from product where product_id = %i' % product_id
        results = self.db.get_results(query)
        return results[0]