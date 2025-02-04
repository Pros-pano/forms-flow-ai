"""This manages form process mapper Schema."""

from marshmallow import EXCLUDE, Schema, fields

from .base_schema import AuditDateTimeSchema


class FormProcessMapperSchema(AuditDateTimeSchema):
    """This class manages form process mapper request and response schema."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Exclude unknown fields in the deserialized output."""

        unknown = EXCLUDE

    id = fields.Str(data_key="id")
    form_id = fields.Str(data_key="formId", required=True)
    form_name = fields.Str(data_key="formName", required=True)
    form_type = fields.Str(data_key="formType")
    parent_form_id = fields.Str(data_key="parentFormId")
    process_key = fields.Str(data_key="processKey")
    process_name = fields.Str(data_key="processName")
    comments = fields.Str(data_key="comments")
    is_anonymous = fields.Bool(data_key="anonymous")
    status = fields.Str(data_key="status", allow_none=True)  # active/inactive
    created_by = fields.Str(data_key="createdBy")
    modified_by = fields.Str(data_key="modifiedBy")
    task_variable = fields.Str(data_key="taskVariables")
    version = fields.Str(data_key="version")
    process_tenant = fields.Str(data_key="processTenant")
    deleted = fields.Boolean(data_key="deleted")
    description = fields.Str(data_key="description")
    prompt_new_version = fields.Bool(data_key="promptNewVersion", dump_only=True)
    is_migrated = fields.Bool(data_key="isMigrated", required=False)


class FormProcessMapperListReqSchema(Schema):
    """This is a general class for paginated request schema."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Exclude unknown fields in the deserialized output."""

        unknown = EXCLUDE

    page_no = fields.Int(data_key="pageNo", required=False, allow_none=True)
    limit = fields.Int(required=False, allow_none=True)


class FormProcessMapperListRequestSchema(FormProcessMapperListReqSchema):
    """This class manages formprocessmapper list request schema."""

    search = fields.Str(data_key="search", required=False)
    sort_by = fields.Str(data_key="sortBy", required=False)
    sort_order = fields.Str(data_key="sortOrder", required=False)
    form_type = fields.Str(data_key="formType", required=False)
    is_active = fields.Bool(data_key="isActive", required=False)
    active_forms = fields.Bool(data_key="activeForms", required=False)
    ignore_designer = fields.Bool(
        data_key="showForOnlyCreateSubmissionUsers", required=False
    )
