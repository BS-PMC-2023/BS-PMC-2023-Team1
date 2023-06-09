from django.test import TestCase
from .models import favoriteExpert, favoriteArticle


class FavoriteExpertModelTest(TestCase):
    def setUp(self):
        self.expert = favoriteExpert.objects.create(expertId=1, userId=1)

    def test_expert_id_field(self):
        field = self.expert._meta.get_field('expertId')
        self.assertEqual(field.get_internal_type(), 'IntegerField')
        self.assertFalse(field.null)
        self.assertFalse(field.blank)

    def test_user_id_field(self):
        field = self.expert._meta.get_field('userId')
        self.assertEqual(field.get_internal_type(), 'IntegerField')
        self.assertFalse(field.null)
        self.assertFalse(field.blank)

    def test_favorite_expert_creation(self):
        self.assertEqual(self.expert.expertId, 1)
        self.assertEqual(self.expert.userId, 1)


class FavoriteArticleModelTest(TestCase):
    def setUp(self):
        self.article = favoriteArticle.objects.create(link='http://example.com', userId=1)

    def test_link_field(self):
        field = self.article._meta.get_field('link')
        self.assertEqual(field.get_internal_type(), 'CharField')
        self.assertEqual(field.max_length, 1000)
        self.assertFalse(field.null)
        self.assertFalse(field.blank)

    def test_user_id_field(self):
        field = self.article._meta.get_field('userId')
        self.assertEqual(field.get_internal_type(), 'IntegerField')
        self.assertFalse(field.null)
        self.assertFalse(field.blank)

    def test_favorite_article_creation(self):
        self.assertEqual(self.article.link, 'http://example.com')
        self.assertEqual(self.article.userId, 1)
