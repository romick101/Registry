#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase

from models import *


class RequestMethodTests(TestCase):
    def setUp(self):
        Request.objects.create(
            answertype='1',
            date='2016-05-12',
            passportid=Inpassport.objects.create(
                series='VF',
                number='344551',
                firstname='Jane',
                secondname='Maria',
                lastname='Doe',
                birthdate='1999-12-12',
                birthplace='London',
                givendate='2015-12-30',
                givenby='London CV'
            ),
            purpose='Work check',
            obtainway='1',
            applicantinfo='Nice person',
            servicenotes='notes',
            taxcode='123424'
        )

    def test_add(self):
        p = Request.objects.get()
        self.assertIsInstance(p, Request)

    def test_delete(self):
        data = Request.objects.get()
        data.delete()
        try:
            obj = Request.objects.get()
        except Request.DoesNotExist:
            obj = None
        self.assertIsNone(obj)

    def test_update(self):
        data = Request.objects.get()
        data.purpose = 'Changed'
        data.save()
        updated_data = Request.objects.get(purpose='Changed')
        self.assertEqual(updated_data.id, data.id)

    def test_delete_cascade(self):
        try:
            request = Request.objects.get(passportid__firstname='Jane')
        except Request.DoesNotExist:
            request = None

        self.assertIsNotNone(request)  # is not None before foreign key delete

        id = request.id

        passport = Inpassport.objects.get(firstname='Jane')
        passport.delete()

        try:
            request = Request.objects.get(pk=id)
        except Request.DoesNotExist:
            request = None

        self.assertIsNone(request)


class InPassportMethodTests(TestCase):
    def setUp(self):
        Inpassport.objects.create(
            series='VF',
            number='344551',
            firstname='Jane',
            secondname='Maria',
            lastname='Doe',
            birthdate='1999-12-12',
            birthplace='London',
            givendate='2015-12-30',
            givenby='London CV'
        )

    def test_add(self):
        p = Inpassport.objects.get()
        self.assertIsInstance(p, Inpassport)

    def test_delete(self):
        data = Inpassport.objects.get()
        data.delete()
        try:
            obj = Inpassport.objects.get()
        except Inpassport.DoesNotExist:
            obj = None
        self.assertIsNone(obj)

    def test_update(self):
        data = Inpassport.objects.get()
        data.firstname = 'Name'
        data.save()
        updated_data = Inpassport.objects.get(firstname='Name')
        self.assertEqual(updated_data.id, data.id)


class RegisteredPassportMethodTests(TestCase):
    def setUp(self):
        Registeredpassport.objects.create(
            series='VF',
            number='344551',
            firstname='Jane',
            secondname='Maria',
            lastname='Doe',
            birthdate='1999-12-12',
            birthplace='London',
            givendate='2015-12-30',
            givenby='London CV'
        )

    def test_add(self):
        p = Registeredpassport.objects.get()
        self.assertIsInstance(p, Registeredpassport)

    def test_delete(self):
        data = Registeredpassport.objects.get()
        data.delete()
        try:
            obj = Registeredpassport.objects.get()
        except Registeredpassport.DoesNotExist:
            obj = None
        self.assertIsNone(obj)

    def test_update(self):
        data = Registeredpassport.objects.get()
        data.firstname = 'Name'
        data.save()
        updated_data = Registeredpassport.objects.get(firstname='Name')
        self.assertEqual(updated_data.id, data.id)


class PersonMethodTests(TestCase):
    def setUp(self):
        Person.objects.create(
            workplace='Roshen',
            workpost='Director',
            checkresult='Checking',
            startingterm='2015-12-01',
            passportid=Registeredpassport.objects.create(
                series='VF',
                number='344551',
                firstname='Jane',
                secondname='Maria',
                lastname='Doe',
                birthdate='1999-12-12',
                birthplace='London',
                givendate='2015-12-30',
                givenby='London CV'
            ),
            taxcode='1242344'
        )

    def test_add(self):
        data = Person.objects.get()
        self.assertIsInstance(data, Person)

    def test_delete(self):
        data = Person.objects.get()
        data.delete()
        try:
            obj = Person.objects.get()
        except Person.DoesNotExist:
            obj = None
        self.assertIsNone(obj)

    def test_update(self):
        data = Person.objects.get()
        data.workplace = 'Changed'
        data.save()
        updated_data = Person.objects.get(
            workplace='Changed'
        )
        self.assertEqual(updated_data.id, data.id)

    def test_delete_cascade(self):
        try:
            person = Person.objects.get(passportid__firstname='Jane')
        except Person.DoesNotExist:
            person = None

        self.assertIsNotNone(person)  # is not None before foreign key delete

        id = person.id

        passport = Registeredpassport.objects.get(firstname='Jane')
        passport.delete()

        try:
            person = Person.objects.get(pk=id)
        except Person.DoesNotExist:
            person = None

        self.assertIsNone(person)


class PositiveReferenceMethodTests(TestCase):
    def setUp(self):
        Positivereference.objects.create(
            requestid=Request.objects.create(
                answertype='1',
                date='2016-05-12',
                passportid=Inpassport.objects.create(
                    series='VF',
                    number='344551',
                    firstname='Jane',
                    secondname='Maria',
                    lastname='Doe',
                    birthdate='1999-12-12',
                    birthplace='London',
                    givendate='2015-12-30',
                    givenby='London CV'
                ),
                purpose='Work check',
                obtainway='1',
                applicantinfo='Nice person',
                servicenotes='notes',
                taxcode='123424'
            ),
            personid=Person.objects.create(
                workplace='Roshen',
                workpost='Director',
                checkresult='Checking',
                startingterm='2015-12-01',
                passportid=Registeredpassport.objects.create(
                    series='VF',
                    number='344551',
                    firstname='Jane',
                    secondname='Maria',
                    lastname='Doe',
                    birthdate='1999-12-12',
                    birthplace='London',
                    givendate='2015-12-30',
                    givenby='London CV'
                ),
                taxcode='1242344'
            ),
            personwhomadereference='first guy',
            personwhosignsreference='second guy',
            personswhosignsreferencepost='director'
        )

    def test_add(self):
        data = Positivereference.objects.get()
        self.assertIsInstance(data, Positivereference)

    def test_delete(self):
        data = Positivereference.objects.get()
        data.delete()
        try:
            obj = Positivereference.objects.get()
        except Positivereference.DoesNotExist:
            obj = None
        self.assertIsNone(obj)

    def test_update(self):
        data = Positivereference.objects.get()
        data.personswhosignsreferencepost = 'Changed'
        data.save()
        updated_data = Positivereference.objects.get(
            personswhosignsreferencepost='Changed'
        )
        self.assertEqual(updated_data.id, data.id)

    def test_delete_cascade(self):
        try:
            positivereference = Positivereference.objects.get(requestid__passportid__firstname='Jane')
        except Positivereference.DoesNotExist:
            positivereference = None

        self.assertIsNotNone(positivereference)  # is not None before foreign key delete

        id = positivereference.id

        request = Request.objects.get(passportid__firstname='Jane')
        request.delete()
        person = Person.objects.get(passportid__firstname='Jane')
        person.delete()

        try:
            person = Person.objects.get(pk=id)
            request = Request.objects.get(pk=id)
        except (Request.DoesNotExist, Person.DoesNotExist):
            person = None
            request = None
        self.assertIsNone(person)
        self.assertIsNone(request)


class NegativeReferenceMethodTests(TestCase):
    def setUp(self):
        Negativereference.objects.create(
            requestid=Request.objects.create(
                answertype='1',
                date='2016-05-12',
                passportid=Inpassport.objects.create(
                    series='VF',
                    number='344551',
                    firstname='Jane',
                    secondname='Maria',
                    lastname='Doe',
                    birthdate='1999-12-12',
                    birthplace='London',
                    givendate='2015-12-30',
                    givenby='London CV'
                ),
                purpose='Work check',
                obtainway='1',
                applicantinfo='Nice person',
                servicenotes='notes',
            ),
            personwhomadereference='first guy',
            personwhosignsreference='second guy',
            personswhosignsreferencepost='director'
        )

    def test_add(self):
        data = Negativereference.objects.get()
        self.assertIsInstance(data, Negativereference)

    def test_delete(self):
        data = Negativereference.objects.get()
        data.delete()
        try:
            obj = Negativereference.objects.get()
        except Negativereference.DoesNotExist:
            obj = None
        self.assertIsNone(obj)

    def test_update(self):
        data = Negativereference.objects.get()
        data.personswhosignsreferencepost = 'Changed'
        data.save()
        updated_data = Negativereference.objects.get(
            personswhosignsreferencepost='Changed'
        )
        self.assertEqual(updated_data.id, data.id)

    def test_delete_cascade(self):
        try:
            ref = Negativereference.objects.get(requestid__passportid__firstname='Jane')
        except Negativereference.DoesNotExist:
            ref = None

        self.assertIsNotNone(ref)  # is not None before foreign key delete

        id = ref.id

        request = Request.objects.get(passportid__firstname='Jane')
        request.delete()

        try:
            request = Request.objects.get(pk=id)
        except Request.DoesNotExist:
            request = None
        self.assertIsNone(request)


class ExtractMethodTests(TestCase):
    def setUp(self):
        Extract.objects.create(
            number='32',
            formingdate='2012-12-12',
            applicantinfo='info',
            requestid=Request.objects.create(
                answertype='1',
                date='2016-05-12',
                passportid=Inpassport.objects.create(
                    series='VF',
                    number='344551',
                    firstname='Jane',
                    secondname='Maria',
                    lastname='Doe',
                    birthdate='1999-12-12',
                    birthplace='London',
                    givendate='2015-12-30',
                    givenby='London CV'
                ),
                purpose='Work check',
                obtainway='1',
                applicantinfo='Nice person',
                servicenotes='notes',
                taxcode='123424'
            ),
            personid=Person.objects.create(
                workplace='Roshen',
                workpost='Director',
                checkresult='Checking',
                startingterm='2015-12-01',
                passportid=Registeredpassport.objects.create(
                    series='VF',
                    number='344551',
                    firstname='Jane',
                    secondname='Maria',
                    lastname='Doe',
                    birthdate='1999-12-12',
                    birthplace='London',
                    givendate='2015-12-30',
                    givenby='London CV'
                ),
                taxcode='1242344'
            ),
            personwhomadeextract='first guy',
            personwhosignsextract='second guy',
            personswhosignsextractpost='director'
        )

    def test_add(self):
        data = Extract.objects.get()
        self.assertIsInstance(data, Extract)

    def test_delete(self):
        data = Extract.objects.get()
        data.delete()
        try:
            obj = Extract.objects.get()
        except Extract.DoesNotExist:
            obj = None
        self.assertIsNone(obj)

    def test_update(self):
        data = Extract.objects.get()
        data.personwhosignsextract='Changed'
        data.save()
        updated_data = Extract.objects.get(
            personwhosignsextract='Changed'
        )
        self.assertEqual(updated_data.id, data.id)

    def test_delete_cascade(self):
        try:
            extract = Extract.objects.get(requestid__passportid__firstname='Jane')
        except Extract.DoesNotExist:
            extract = None

        self.assertIsNotNone(extract)  # is not None before foreign key delete

        id = extract.id

        request = Request.objects.get(passportid__firstname='Jane')
        request.delete()
        person = Person.objects.get(passportid__firstname='Jane')
        person.delete()

        try:
            person = Person.objects.get(pk=id)
            request = Request.objects.get(pk=id)
        except (Request.DoesNotExist, Person.DoesNotExist):
            person = None
            request = None
        self.assertIsNone(person)
        self.assertIsNone(request)
