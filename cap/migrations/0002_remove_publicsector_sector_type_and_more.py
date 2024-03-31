# Generated by Django 4.1.7 on 2024-03-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicsector',
            name='sector_type',
        ),
        migrations.RemoveField(
            model_name='report',
            name='location',
        ),
        migrations.RemoveField(
            model_name='report',
            name='public_sector',
        ),
        migrations.AddField(
            model_name='report',
            name='city',
            field=models.CharField(choices=[('Tripoli', 'طرابلس'), ('Beirut', 'بيروت'), ('Sidon', 'صيدا'), ('Tyre', 'صور'), ('Borj Hammoud', 'برج حمود'), ('El Minié', 'المنية'), ('Aaley', 'عاليه'), ('Joünié', 'جونية'), ('Zahlé', 'زحلة'), ('Nabatîyé', 'النبطية'), ('Borj el Qoblé', 'برج القبلة'), ('El Ghâzîyé', 'الغازية'), ('Qabb Eliâs', 'قب الياس'), ('Batroûn', 'بترون'), ('Jbaïl', 'جبيل'), ('Barr Eliâs', 'بر الياس'), ('Zghartā', 'زغرتا'), ('Bent Jbaïl', 'بنت جبيل'), ('Chmistâr', 'شمسطار'), ('Qornet Chahouâne', 'قرنة شهوان'), ('Baalbek', 'بعلبك'), ('El Bâzoûrîyé', 'البازورية'), ('Baaqlîne', 'باقلين'), ('Kahhalé', 'كحالة'), ('Barja', 'برجا'), ('Bteghrîne', 'بتغرين'), ('Sarafand', 'صرفند'), ('Srîfa', 'صريفا'), ('Qâna', 'قانا'), ('Ed Dâmoûr', 'الدامور'), ('Kfar Aabîda', 'كفر عبيدا'), ('Baabda', 'بعبدا'), ('El Qalamoûn', 'القلمون'), ('Ej Jmaïlîyé', 'اج جميلية'), ('Nahr Ibrâhîm', 'نهر ابراهيم'), ('Halba', 'حلبا'), ('Zakrît', 'زكريت'), ('Saoufar', 'صوفر'), ('Borj Rahhâl', 'برج رحال'), ('Jdaidet el Matn', 'جديدة المتن'), ('Sîr ed Danniyé', 'سير الدنية'), ('Jezzîne', 'جزين')], default='بيروت', max_length=100),
        ),
        migrations.AddField(
            model_name='report',
            name='public_sector_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='report',
            name='public_sector_type',
            field=models.CharField(choices=[('hospitals', 'مستشفيات'), ('ministries', 'وزارات'), ('institutions', 'مؤسسات'), ('banks', 'بنوك'), ('prisons', 'سجون'), ('courts', 'محاكم'), ('universities', 'جامعات'), ('military', 'جيش'), ('police', 'شرطة'), ('general_security', 'الأمن العام')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='report',
            name='street',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='impact_level',
            field=models.CharField(choices=[('فردي', 'فردي'), ('مجتمعي', 'مجتمعي'), ('وطني', 'وطني')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='incident_frequency',
            field=models.CharField(choices=[('مرة واحدة', 'مرة واحدة'), ('شهري', 'شهري'), ('أسبوعي', 'أسبوعي'), ('يومي', 'يومي')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_source',
            field=models.CharField(choices=[('مباشر', 'مباشر'), ('غير مباشر', 'غير مباشر'), ('مجهول', 'مجهول')], default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='PublicSector',
        ),
        migrations.DeleteModel(
            name='SectorType',
        ),
    ]