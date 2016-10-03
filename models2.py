# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Batch(models.Model):
    bid = models.IntegerField(primary_key=True)
    token = models.CharField(max_length=64)
    timestamp = models.IntegerField()
    batch = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch'


class BlockContent(models.Model):
    revision_id = models.IntegerField(unique=True, blank=True, null=True)
    type = models.CharField(max_length=32)
    uuid = models.CharField(unique=True, max_length=128)
    langcode = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'block_content'


class BlockContentBody(models.Model):
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.IntegerField()
    revision_id = models.IntegerField()
    langcode = models.CharField(max_length=32)
    delta = models.IntegerField()
    body_value = models.TextField()
    body_summary = models.TextField(blank=True, null=True)
    body_format = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block_content__body'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)


class BlockContentFieldData(models.Model):
    id = models.IntegerField()
    revision_id = models.IntegerField()
    type = models.CharField(max_length=32)
    langcode = models.CharField(max_length=12)
    info = models.CharField(max_length=255, blank=True, null=True)
    changed = models.IntegerField(blank=True, null=True)
    revision_translation_affected = models.IntegerField(blank=True, null=True)
    default_langcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'block_content_field_data'
        unique_together = (('id', 'langcode'),)


class BlockContentFieldRevision(models.Model):
    id = models.IntegerField()
    revision_id = models.IntegerField()
    langcode = models.CharField(max_length=12)
    info = models.CharField(max_length=255, blank=True, null=True)
    changed = models.IntegerField(blank=True, null=True)
    revision_translation_affected = models.IntegerField(blank=True, null=True)
    default_langcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'block_content_field_revision'
        unique_together = (('revision_id', 'langcode'),)


class BlockContentRevision(models.Model):
    id = models.IntegerField()
    revision_id = models.AutoField(primary_key=True)
    langcode = models.CharField(max_length=12)
    revision_log = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block_content_revision'


class BlockContentRevisionBody(models.Model):
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.IntegerField()
    revision_id = models.IntegerField()
    langcode = models.CharField(max_length=32)
    delta = models.IntegerField()
    body_value = models.TextField()
    body_summary = models.TextField(blank=True, null=True)
    body_format = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block_content_revision__body'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)


class CacheBootstrap(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.DecimalField(max_digits=14, decimal_places=3)
    serialized = models.SmallIntegerField()
    tags = models.TextField(blank=True, null=True)
    checksum = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cache_bootstrap'


class CacheConfig(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.DecimalField(max_digits=14, decimal_places=3)
    serialized = models.SmallIntegerField()
    tags = models.TextField(blank=True, null=True)
    checksum = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cache_config'


class CacheContainer(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.DecimalField(max_digits=14, decimal_places=3)
    serialized = models.SmallIntegerField()
    tags = models.TextField(blank=True, null=True)
    checksum = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cache_container'


class CacheData(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.DecimalField(max_digits=14, decimal_places=3)
    serialized = models.SmallIntegerField()
    tags = models.TextField(blank=True, null=True)
    checksum = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cache_data'


class CacheDefault(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.DecimalField(max_digits=14, decimal_places=3)
    serialized = models.SmallIntegerField()
    tags = models.TextField(blank=True, null=True)
    checksum = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cache_default'


class CacheDiscovery(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.DecimalField(max_digits=14, decimal_places=3)
    serialized = models.SmallIntegerField()
    tags = models.TextField(blank=True, null=True)
    checksum = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cache_discovery'


class CacheDynamicPageCache(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.DecimalField(max_digits=14, decimal_places=3)
    serialized = models.SmallIntegerField()
    tags = models.TextField(blank=True, null=True)
    checksum = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cache_dynamic_page_cache'


class CacheEntity(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.DecimalField(max_digits=14, decimal_places=3)
    serialized = models.SmallIntegerField()
    tags = models.TextField(blank=True, null=True)
    checksum = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cache_entity'


class CacheMenu(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.DecimalField(max_digits=14, decimal_places=3)
    serialized = models.SmallIntegerField()
    tags = models.TextField(blank=True, null=True)
    checksum = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cache_menu'


class CacheRender(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.DecimalField(max_digits=14, decimal_places=3)
    serialized = models.SmallIntegerField()
    tags = models.TextField(blank=True, null=True)
    checksum = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cache_render'


class Cachetags(models.Model):
    tag = models.CharField(primary_key=True, max_length=255)
    invalidations = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cachetags'


class Card(models.Model):
    card_id = models.CharField(max_length=30)
    credit = models.IntegerField()
    serial = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'card'


class CasLoginData(models.Model):
    sid = models.CharField(primary_key=True, max_length=128)
    plainsid = models.CharField(max_length=128)
    ticket = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'cas_login_data'


class CasPgtStorage(models.Model):
    pgt_iou = models.CharField(primary_key=True, max_length=256)
    pgt = models.CharField(max_length=256)
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cas_pgt_storage'
        unique_together = (('pgt_iou', 'pgt'),)


class Comment(models.Model):
    cid = models.AutoField(primary_key=True)
    comment_type = models.CharField(max_length=32)
    uuid = models.CharField(unique=True, max_length=128)
    langcode = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'comment'


class CommentCommentBody(models.Model):
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.IntegerField()
    revision_id = models.IntegerField()
    langcode = models.CharField(max_length=32)
    delta = models.IntegerField()
    comment_body_value = models.TextField()
    comment_body_format = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment__comment_body'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)


class CommentEntityStatistics(models.Model):
    entity_id = models.IntegerField()
    entity_type = models.CharField(max_length=32)
    field_name = models.CharField(max_length=32)
    cid = models.IntegerField()
    last_comment_timestamp = models.IntegerField()
    last_comment_name = models.CharField(max_length=60, blank=True, null=True)
    last_comment_uid = models.IntegerField()
    comment_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comment_entity_statistics'
        unique_together = (('entity_id', 'entity_type', 'field_name'),)


class CommentFieldData(models.Model):
    cid = models.IntegerField()
    comment_type = models.CharField(max_length=32)
    langcode = models.CharField(max_length=12)
    pid = models.IntegerField(blank=True, null=True)
    entity_id = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=64, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    mail = models.CharField(max_length=254, blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    hostname = models.CharField(max_length=128, blank=True, null=True)
    created = models.IntegerField()
    changed = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    thread = models.CharField(max_length=255)
    entity_type = models.CharField(max_length=32, blank=True, null=True)
    field_name = models.CharField(max_length=32, blank=True, null=True)
    default_langcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comment_field_data'
        unique_together = (('cid', 'langcode'),)


class Config(models.Model):
    collection = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config'
        unique_together = (('collection', 'name'),)


class Data(models.Model):
    card_id = models.CharField(max_length=30)
    machine_id = models.CharField(max_length=30)
    product = models.CharField(max_length=25)
    price = models.IntegerField()
    date_time = models.DateTimeField()
    payment_id = models.CharField(max_length=30)
    mode = models.CharField(max_length=30)
    name_cust = models.CharField(max_length=30)
    credit = models.CharField(max_length=30)
    coil = models.CharField(max_length=10)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'data'


class ErrorLog(models.Model):
    machine_id = models.CharField(db_column='Machine_id', max_length=30)  # Field name made lowercase.
    error = models.CharField(max_length=30)
    response = models.CharField(max_length=30)
    received = models.CharField(max_length=30)
    context = models.CharField(max_length=60)
    date_time = models.DateTimeField()
    s_no_field = models.AutoField(db_column='S. no.', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'error_log'


class FileManaged(models.Model):
    fid = models.AutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=128)
    langcode = models.CharField(max_length=12)
    uid = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    uri = models.CharField(max_length=255)
    filemime = models.CharField(max_length=255, blank=True, null=True)
    filesize = models.BigIntegerField(blank=True, null=True)
    status = models.IntegerField()
    created = models.IntegerField(blank=True, null=True)
    changed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'file_managed'


class FileUsage(models.Model):
    fid = models.IntegerField()
    module = models.CharField(max_length=50)
    type = models.CharField(max_length=64)
    id = models.CharField(max_length=64)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'file_usage'
        unique_together = (('fid', 'type', 'id', 'module'),)


class History(models.Model):
    uid = models.IntegerField()
    nid = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'history'
        unique_together = (('uid', 'nid'),)


class KeyValue(models.Model):
    collection = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'key_value'
        unique_together = (('collection', 'name'),)


class KeyValueExpire(models.Model):
    collection = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    value = models.TextField()
    expire = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'key_value_expire'
        unique_together = (('collection', 'name'),)


class MenuLinkContent(models.Model):
    bundle = models.CharField(max_length=32)
    uuid = models.CharField(unique=True, max_length=128)
    langcode = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'menu_link_content'


class MenuLinkContentData(models.Model):
    id = models.IntegerField()
    bundle = models.CharField(max_length=32)
    langcode = models.CharField(max_length=12)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    menu_name = models.CharField(max_length=255, blank=True, null=True)
    link_uri = models.CharField(db_column='link__uri', max_length=2048, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    link_title = models.CharField(db_column='link__title', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    link_options = models.TextField(db_column='link__options', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    external = models.IntegerField(blank=True, null=True)
    rediscover = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    expanded = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    parent = models.CharField(max_length=255, blank=True, null=True)
    changed = models.IntegerField(blank=True, null=True)
    default_langcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'menu_link_content_data'
        unique_together = (('id', 'langcode'),)


class MenuTree(models.Model):
    menu_name = models.CharField(max_length=32)
    mlid = models.AutoField(primary_key=True)
    id = models.CharField(unique=True, max_length=255)
    parent = models.CharField(max_length=255)
    route_name = models.CharField(max_length=255, blank=True, null=True)
    route_param_key = models.CharField(max_length=255, blank=True, null=True)
    route_parameters = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    options = models.TextField(blank=True, null=True)
    provider = models.CharField(max_length=50)
    enabled = models.SmallIntegerField()
    discovered = models.SmallIntegerField()
    expanded = models.SmallIntegerField()
    weight = models.IntegerField()
    metadata = models.TextField(blank=True, null=True)
    has_children = models.SmallIntegerField()
    depth = models.SmallIntegerField()
    p1 = models.IntegerField()
    p2 = models.IntegerField()
    p3 = models.IntegerField()
    p4 = models.IntegerField()
    p5 = models.IntegerField()
    p6 = models.IntegerField()
    p7 = models.IntegerField()
    p8 = models.IntegerField()
    p9 = models.IntegerField()
    form_class = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_tree'


class Node(models.Model):
    nid = models.AutoField(primary_key=True)
    vid = models.IntegerField(unique=True, blank=True, null=True)
    type = models.CharField(max_length=32)
    uuid = models.CharField(unique=True, max_length=128)
    langcode = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'node'


class NodeBody(models.Model):
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.IntegerField()
    revision_id = models.IntegerField()
    langcode = models.CharField(max_length=32)
    delta = models.IntegerField()
    body_value = models.TextField()
    body_summary = models.TextField(blank=True, null=True)
    body_format = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node__body'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)


class NodeComment(models.Model):
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.IntegerField()
    revision_id = models.IntegerField()
    langcode = models.CharField(max_length=32)
    delta = models.IntegerField()
    comment_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'node__comment'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)


class NodeFieldImage(models.Model):
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.IntegerField()
    revision_id = models.IntegerField()
    langcode = models.CharField(max_length=32)
    delta = models.IntegerField()
    field_image_target_id = models.IntegerField()
    field_image_alt = models.CharField(max_length=512, blank=True, null=True)
    field_image_title = models.CharField(max_length=1024, blank=True, null=True)
    field_image_width = models.IntegerField(blank=True, null=True)
    field_image_height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node__field_image'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)


class NodeFieldTags(models.Model):
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.IntegerField()
    revision_id = models.IntegerField()
    langcode = models.CharField(max_length=32)
    delta = models.IntegerField()
    field_tags_target_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'node__field_tags'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)


class NodeAccess(models.Model):
    nid = models.IntegerField()
    langcode = models.CharField(max_length=12)
    fallback = models.IntegerField()
    gid = models.IntegerField()
    realm = models.CharField(max_length=255)
    grant_view = models.IntegerField()
    grant_update = models.IntegerField()
    grant_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'node_access'
        unique_together = (('nid', 'gid', 'realm', 'langcode'),)


class NodeFieldData(models.Model):
    nid = models.IntegerField()
    vid = models.IntegerField()
    type = models.CharField(max_length=32)
    langcode = models.CharField(max_length=12)
    title = models.CharField(max_length=255)
    uid = models.IntegerField()
    status = models.IntegerField()
    created = models.IntegerField()
    changed = models.IntegerField()
    promote = models.IntegerField()
    sticky = models.IntegerField()
    revision_translation_affected = models.IntegerField(blank=True, null=True)
    default_langcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'node_field_data'
        unique_together = (('nid', 'langcode'),)


class NodeFieldRevision(models.Model):
    nid = models.IntegerField()
    vid = models.IntegerField()
    langcode = models.CharField(max_length=12)
    title = models.CharField(max_length=255, blank=True, null=True)
    uid = models.IntegerField()
    status = models.IntegerField()
    created = models.IntegerField(blank=True, null=True)
    changed = models.IntegerField(blank=True, null=True)
    promote = models.IntegerField(blank=True, null=True)
    sticky = models.IntegerField(blank=True, null=True)
    revision_translation_affected = models.IntegerField(blank=True, null=True)
    default_langcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'node_field_revision'
        unique_together = (('vid', 'langcode'),)


class NodeRevision(models.Model):
    nid = models.IntegerField()
    vid = models.AutoField(primary_key=True)
    langcode = models.CharField(max_length=12)
    revision_timestamp = models.IntegerField(blank=True, null=True)
    revision_uid = models.IntegerField(blank=True, null=True)
    revision_log = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_revision'


class NodeRevisionBody(models.Model):
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.IntegerField()
    revision_id = models.IntegerField()
    langcode = models.CharField(max_length=32)
    delta = models.IntegerField()
    body_value = models.TextField()
    body_summary = models.TextField(blank=True, null=True)
    body_format = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_revision__body'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)


class NodeRevisionComment(models.Model):
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.IntegerField()
    revision_id = models.IntegerField()
    langcode = models.CharField(max_length=32)
    delta = models.IntegerField()
    comment_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'node_revision__comment'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)


class NodeRevisionFieldImage(models.Model):
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.IntegerField()
    revision_id = models.IntegerField()
    langcode = models.CharField(max_length=32)
    delta = models.IntegerField()
    field_image_target_id = models.IntegerField()
    field_image_alt = models.CharField(max_length=512, blank=True, null=True)
    field_image_title = models.CharField(max_length=1024, blank=True, null=True)
    field_image_width = models.IntegerField(blank=True, null=True)
    field_image_height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_revision__field_image'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)


class NodeRevisionFieldTags(models.Model):
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.IntegerField()
    revision_id = models.IntegerField()
    langcode = models.CharField(max_length=32)
    delta = models.IntegerField()
    field_tags_target_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'node_revision__field_tags'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)


class Queue(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'queue'


class Router(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    path = models.CharField(max_length=255)
    pattern_outline = models.CharField(max_length=255)
    fit = models.IntegerField()
    route = models.TextField(blank=True, null=True)
    number_parts = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'router'


class SearchDataset(models.Model):
    sid = models.IntegerField()
    langcode = models.CharField(max_length=12)
    type = models.CharField(max_length=64)
    data = models.TextField()
    reindex = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'search_dataset'
        unique_together = (('sid', 'langcode', 'type'),)


class SearchIndex(models.Model):
    word = models.CharField(max_length=50)
    sid = models.IntegerField()
    langcode = models.CharField(max_length=12)
    type = models.CharField(max_length=64)
    score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_index'
        unique_together = (('word', 'sid', 'langcode', 'type'),)


class SearchTotal(models.Model):
    word = models.CharField(primary_key=True, max_length=50)
    count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_total'


class Semaphore(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    value = models.CharField(max_length=255)
    expire = models.FloatField()

    class Meta:
        managed = False
        db_table = 'semaphore'


class Sequences(models.Model):
    value = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'sequences'


class Sessions(models.Model):
    uid = models.IntegerField()
    sid = models.CharField(primary_key=True, max_length=128)
    hostname = models.CharField(max_length=128)
    timestamp = models.IntegerField()
    session = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions'


class Shortcut(models.Model):
    shortcut_set = models.CharField(max_length=32)
    uuid = models.CharField(unique=True, max_length=128)
    langcode = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'shortcut'


class ShortcutFieldData(models.Model):
    id = models.IntegerField()
    shortcut_set = models.CharField(max_length=32)
    langcode = models.CharField(max_length=12)
    title = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    link_uri = models.CharField(db_column='link__uri', max_length=2048, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    link_title = models.CharField(db_column='link__title', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    link_options = models.TextField(db_column='link__options', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    default_langcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shortcut_field_data'
        unique_together = (('id', 'langcode'),)


class ShortcutSetUsers(models.Model):
    uid = models.IntegerField(primary_key=True)
    set_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'shortcut_set_users'


class TaxonomyIndex(models.Model):
    nid = models.IntegerField()
    tid = models.IntegerField()
    status = models.IntegerField()
    sticky = models.IntegerField(blank=True, null=True)
    created = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'taxonomy_index'
        unique_together = (('nid', 'tid'),)


class TaxonomyTermData(models.Model):
    tid = models.AutoField(primary_key=True)
    vid = models.CharField(max_length=32)
    uuid = models.CharField(unique=True, max_length=128)
    langcode = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'taxonomy_term_data'


class TaxonomyTermFieldData(models.Model):
    tid = models.IntegerField()
    vid = models.CharField(max_length=32)
    langcode = models.CharField(max_length=12)
    name = models.CharField(max_length=255)
    description_value = models.TextField(db_column='description__value', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    description_format = models.CharField(db_column='description__format', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    weight = models.IntegerField()
    changed = models.IntegerField(blank=True, null=True)
    default_langcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'taxonomy_term_field_data'
        unique_together = (('tid', 'langcode'),)


class TaxonomyTermHierarchy(models.Model):
    tid = models.IntegerField()
    parent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'taxonomy_term_hierarchy'
        unique_together = (('tid', 'parent'),)


class UrlAlias(models.Model):
    pid = models.AutoField(primary_key=True)
    source = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    langcode = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'url_alias'


class UserRoles(models.Model):
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.IntegerField()
    revision_id = models.IntegerField()
    langcode = models.CharField(max_length=32)
    delta = models.IntegerField()
    roles_target_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user__roles'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)


class UserUserPicture(models.Model):
    bundle = models.CharField(max_length=128)
    deleted = models.IntegerField()
    entity_id = models.IntegerField()
    revision_id = models.IntegerField()
    langcode = models.CharField(max_length=32)
    delta = models.IntegerField()
    user_picture_target_id = models.IntegerField()
    user_picture_alt = models.CharField(max_length=512, blank=True, null=True)
    user_picture_title = models.CharField(max_length=1024, blank=True, null=True)
    user_picture_width = models.IntegerField(blank=True, null=True)
    user_picture_height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user__user_picture'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)


class Users(models.Model):
    uid = models.IntegerField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=128)
    langcode = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'users'


class UsersData(models.Model):
    uid = models.IntegerField()
    module = models.CharField(max_length=50)
    name = models.CharField(max_length=128)
    value = models.TextField(blank=True, null=True)
    serialized = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_data'
        unique_together = (('uid', 'module', 'name'),)


class UsersFieldData(models.Model):
    uid = models.IntegerField()
    langcode = models.CharField(max_length=12)
    preferred_langcode = models.CharField(max_length=12, blank=True, null=True)
    preferred_admin_langcode = models.CharField(max_length=12, blank=True, null=True)
    name = models.CharField(max_length=60)
    pass_field = models.CharField(db_column='pass', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    mail = models.CharField(max_length=254, blank=True, null=True)
    timezone = models.CharField(max_length=32, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created = models.IntegerField()
    changed = models.IntegerField(blank=True, null=True)
    access = models.IntegerField()
    login = models.IntegerField(blank=True, null=True)
    init = models.CharField(max_length=254, blank=True, null=True)
    default_langcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_field_data'
        unique_together = (('uid', 'langcode'), ('name', 'langcode'),)


class Watchdog(models.Model):
    wid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    type = models.CharField(max_length=64)
    message = models.TextField()
    variables = models.TextField()
    severity = models.IntegerField()
    link = models.TextField(blank=True, null=True)
    location = models.TextField()
    referer = models.TextField(blank=True, null=True)
    hostname = models.CharField(max_length=128)
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'watchdog'
