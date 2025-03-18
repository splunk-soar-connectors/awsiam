# File: awsiam_consts.py
#
# Copyright (c) 2018-2025 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
AWSIAM_ACCESS_KEY = "access_key"
AWSIAM_SECRET_KEY = "secret_key"  # pragma: allowlist secret
AWSIAM_SERVICE = "iam"
AWSIAM_HOST = "iam.amazonaws.com"
AWSIAM_SERVER_URL = "https://iam.amazonaws.com"
AWSIAM_REGION = "us-east-1"
AWSIAM_SIGNATURE_V4 = "AWS4"
AWSIAM_API_VERSION = "2010-05-08"
AWSIAM_SIGNATURE_V4_REQUEST = "aws4_request"
AWSIAM_REQUESTS_SIGNING_ALGO = "AWS4-HMAC-SHA256"
AWSIAM_SIGNED_HEADERS = "host;x-amz-date"
AWSIAM_TEST_CONNECTIVITY_ENDPOINT = "GetUser"
AWSIAM_GET_USER_GROUPS_ENDPOINT = "ListGroupsForUser"
AWSIAM_GET_USER_POLICIES_ENDPOINT = "ListAttachedUserPolicies"
AWSIAM_DISABLE_USER_ENDPOINT = "DeleteLoginProfile"
AWSIAM_ENABLE_USER_ENDPOINT = "CreateLoginProfile"
AWSIAM_ADD_USER_TO_GROUP_ENDPOINT = "AddUserToGroup"
AWSIAM_REMOVE_USER_FROM_GROUP_ENDPOINT = "RemoveUserFromGroup"
AWSIAM_ADD_ROLE_ENDPOINT = "CreateRole"
AWSIAM_DELETE_USER_ENDPOINT = "DeleteUser"
AWSIAM_ATTACH_ROLE_POLICY_ENDPOINT = "AttachRolePolicy"
AWSIAM_DETACH_ROLE_POLICY_ENDPOINT = "DetachRolePolicy"
AWSIAM_ATTACH_USER_POLICY_ENDPOINT = "AttachUserPolicy"
AWSIAM_DETACH_USER_POLICY_ENDPOINT = "DetachUserPolicy"
AWSIAM_LIST_ROLES_ENDPOINT = "ListRoles"
AWSIAM_LIST_USERS_ENDPOINT = "ListUsers"
AWSIAM_LIST_ACCESS_KEYS_ENDPOINT = "ListAccessKeys"
AWSIAM_DELETE_ACCESS_KEYS_ENDPOINT = "DeleteAccessKey"
AWSIAM_GET_ROLE_INSTANCE_PROFILES_ENDPOINT = "ListInstanceProfilesForRole"
AWSIAM_DETACH_ROLE_INSTANCE_PROFILE_ENDPOINT = "RemoveRoleFromInstanceProfile"
AWSIAM_GET_ROLE_POLICIES_ENDPOINT = "ListAttachedRolePolicies"
AWSIAM_DELETE_ROLE_ENDPOINT = "DeleteRole"
AWSIAM_LIST_USERS_OF_GROUP_ENDPOINT = "GetGroup"
AWSIAM_UPDATE_ACCESS_KEYS_ENDPOINT = "UpdateAccessKey"
AWSIAM_ADD_ROLE_INSTANCE_PROFILE_ENDPOINT = "CreateInstanceProfile"
AWSIAM_ATTACH_ROLE_INSTANCE_PROFILE_ENDPOINT = "AddRoleToInstanceProfile"
AWSIAM_GET_ROLE_ENDPOINT = "GetRole"
AWSIAM_GET_ROLE_INSTANCE_PROFILE_ENDPOINT = "GetInstanceProfile"
AWSIAM_DELETE_INSTANCE_PROFILE_ENDPOINT = "DeleteInstanceProfile"
AWSIAM_LIST_GROUPS_ENDPOINT = "ListGroups"
AWSIAM_PARAM_USERNAME = "username"
AWSIAM_PARAM_PASSWORD = "password"  # pragma: allowlist secret
AWSIAM_PARAM_GROUP_NAME = "group_name"
AWSIAM_PARAM_ROLE_NAME = "role_name"
AWSIAM_PARAM_ROLE_POLICY_DOC = "role_policy_document"
AWSIAM_PARAM_ROLE_PATH = "role_path"
AWSIAM_PARAM_POLICY_ARN = "policy_arn"
AWSIAM_PARAM_USER_PATH = "user_path"
AWSIAM_PARAM_ENABLE_ACCESS_KEYS = "enable_access_keys"
AWSIAM_PARAM_DISABLE_ACCESS_KEYS = "disable_access_keys"
AWSIAM_PARAM_GROUP_PATH = "group_path"
AWSIAM_JSON_IS_TRUNCATED = "IsTruncated"
AWSIAM_JSON_MARKER = "Marker"
AWSIAM_JSON_AMZ_DATE = "x-amz-date"
AWSIAM_JSON_STS_TOKEN = "X-Amz-Security-Token"
AWSIAM_JSON_AUTHORIZATION = "Authorization"
AWSIAM_JSON_PATH = "Path"
AWSIAM_JSON_ACTION = "Action"
AWSIAM_JSON_VERSION = "Version"
AWSIAM_JSON_STATUS = "Status"
AWSIAM_JSON_MEMBER = "member"
AWSIAM_JSON_USERNAME = "UserName"
AWSIAM_JSON_PASSWORD = "Password"  # pragma: allowlist secret
AWSIAM_JSON_INACTIVE = "Inactive"
AWSIAM_JSON_ACTIVE = "Active"
AWSIAM_JSON_GROUPS = "Groups"
AWSIAM_JSON_GROUP_NAME = "GroupName"
AWSIAM_JSON_ROLES = "Roles"
AWSIAM_JSON_USERS = "Users"
AWSIAM_JSON_PATHS_GROUPS = "GroupsPaths"
AWSIAM_JSON_GROUP_USERS = "GroupUsers"
AWSIAM_JSON_POLICIES = "AttachedPolicies"
AWSIAM_JSON_ROLE_POLICIES = "AttachedRolePolicies"
AWSIAM_JSON_INSTANCE_PROFILES = "InstanceProfiles"
AWSIAM_JSON_RESPONSE_METADATA = "ResponseMetadata"
AWSIAM_JSON_LIST_RESPONSE = "ListResponse"
AWSIAM_JSON_REQUEST_ID = "RequestId"
AWSIAM_JSON_LOGIN_PROFILE = "LoginProfile"
AWSIAM_JSON_ERROR = "Error"
AWSIAM_JSON_ERROR_TYPE = "Type"
AWSIAM_JSON_ERROR_CODE = "Code"
AWSIAM_JSON_ERROR_MSG = "Message"
AWSIAM_JSON_ERROR_RESPONSE = "ErrorResponse"
AWSIAM_JSON_ROLE = "Role"
AWSIAM_JSON_ATTACHED = "attached"
AWSIAM_JSON_DETACHED = "detached"
AWSIAM_JSON_ROLE_NAME = "RoleName"
AWSIAM_JSON_INSTANCE_PROFILE_NAME = "InstanceProfileName"
AWSIAM_JSON_ROLE_PATH = "Path"
AWSIAM_JSON_POLICY_ARN = "PolicyArn"
AWSIAM_JSON_USER_PATH_PREFIX = "PathPrefix"
AWSIAM_JSON_ACCESS_KEYS = "AccessKeyMetadata"
AWSIAM_JSON_ACCESS_KEY_ID = "AccessKeyId"
AWSIAM_JSON_ASSUME_POLICY_DOCUMENT = "AssumeRolePolicyDocument"
AWSIAM_JSON_ADD_USER_TO_GROUP_RESPONSE = "AddUserToGroupResponse"
AWSIAM_JSON_REMOVE_USER_FROM_GROUP_RESPONSE = "RemoveUserFromGroupResponse"
AWSIAM_JSON_LIST_GROUPS_FOR_USER_RESPONSE = "ListGroupsForUserResponse"
AWSIAM_JSON_LIST_GROUPS_FOR_USER_RESULT = "ListGroupsForUserResult"
AWSIAM_JSON_LIST_POLICIES_FOR_USER_RESPONSE = "ListAttachedUserPoliciesResponse"
AWSIAM_JSON_LIST_POLICIES_FOR_USER_RESULT = "ListAttachedUserPoliciesResult"
AWSIAM_JSON_DELETE_LOGIN_PROFILE_RESPONSE = "DeleteLoginProfileResponse"
AWSIAM_JSON_LIST_ROLES_RESPONSE = "ListRolesResponse"
AWSIAM_JSON_LIST_ROLES_RESULT = "ListRolesResult"
AWSIAM_JSON_LIST_USERS_RESPONSE = "ListUsersResponse"
AWSIAM_JSON_LIST_USERS_RESULT = "ListUsersResult"
AWSIAM_JSON_CREATE_LOGIN_PROFILE_RESPONSE = "CreateLoginProfileResponse"
AWSIAM_JSON_CREATE_LOGIN_PROFILE_RESULT = "CreateLoginProfileResult"
AWSIAM_JSON_CREATE_ROLE_RESPONSE = "CreateRoleResponse"
AWSIAM_JSON_CREATE_ROLE_RESULT = "CreateRoleResult"
AWSIAM_JSON_ATTACH_ROLE_POLICY_RESPONSE = "AttachRolePolicyResponse"
AWSIAM_JSON_DETACH_ROLE_POLICY_RESPONSE = "DetachRolePolicyResponse"
AWSIAM_JSON_ATTACH_USER_POLICY_RESPONSE = "AttachUserPolicyResponse"
AWSIAM_JSON_DETACH_USER_POLICY_RESPONSE = "DetachUserPolicyResponse"
AWSIAM_JSON_DELETE_USER_RESPONSE = "DeleteUserResponse"
AWSIAM_JSON_LIST_ACCESS_KEYS_RESPONSE = "ListAccessKeysResponse"
AWSIAM_JSON_LIST_ACCESS_KEYS_RESULT = "ListAccessKeysResult"
AWSIAM_JSON_LIST_INSTANCE_PROFILES_RESPONSE = "ListInstanceProfilesForRoleResponse"
AWSIAM_JSON_LIST_INSTANCE_PROFILES_RESULT = "ListInstanceProfilesForRoleResult"
AWSIAM_JSON_LIST_ROLE_POLICIES_RESPONSE = "ListAttachedRolePoliciesResponse"
AWSIAM_JSON_LIST_ROLE_POLICIES_RESULT = "ListAttachedRolePoliciesResult"
AWSIAM_JSON_DELETE_ROLE_RESPONSE = "DeleteRoleResponse"
AWSIAM_JSON_GET_GROUP_RESPONSE = "GetGroupResponse"
AWSIAM_JSON_GET_GROUP_RESULT = "GetGroupResult"
AWSIAM_JSON_UPDATE_ACCESS_KEY_RESPONSE = "UpdateAccessKeyResponse"
AWSIAM_JSON_ADD_ROLE_INSTANCE_PROFILE_RESPONSE = "AddRoleToInstanceProfileResponse"
AWSIAM_JSON_LIST_GROUPS_RESPONSE = "ListGroupsResponse"
AWSIAM_JSON_LIST_GROUPS_RESULT = "ListGroupsResult"
AWSIAM_TEST_CONNECTIVITY_PASSED_MSG = "Test Connectivity Passed"
AWSIAM_TEST_CONNECTIVITY_FAILED_MSG = "Test Connectivity Failed"
AWSIAM_CONNECTING_ENDPOINT_MSG = "Connecting to an endpoint"
AWSIAM_USER_DISABLED_MSG = "User {username} disabled successfully"
AWSIAM_USER_ENABLED_MSG = "User {username} enabled successfully"
AWSIAM_USER_ADDED_TO_GROUP_MSG = "User {username} successfully added to the group {group_name}"
AWSIAM_USER_REMOVED_FROM_GROUP_MSG = "User {username} successfully removed from the group {group_name}"
AWSIAM_ADD_ROLE_MSG = "Role {role_name} successfully added in AWS account"
AWSIAM_INVALID_ROLE_PATH_MSG = 'Role path always starts and ends with "/". Hence, given role path is invalid.'
AWSIAM_INVALID_USER_PATH_MSG = 'User path always starts and ends with "/". Hence, given user path is invalid.'
AWSIAM_INVALID_GROUP_PATH_MSG = 'Group path always starts and ends with "/". Hence, given group path is invalid.'
AWSIAM_ATTACH_ROLE_POLICY_MSG = "Policy with ARN {policy_arn} successfully attached with role {role_name}"
AWSIAM_DETACH_ROLE_POLICY_MSG = "Policy with ARN {policy_arn} successfully detached from role {role_name}"
AWSIAM_ATTACH_USER_POLICY_MSG = "Policy with ARN {policy_arn} successfully assigned to user {username}"
AWSIAM_DETACH_USER_POLICY_MSG = "Policy with ARN {policy_arn} successfully removed from user {username}"
AWSIAM_USER_DELETED_MSG = (
    "User {username} deleted successfully along with all its associations with login profile, access keys, groups, and policies"
)
AWSIAM_ROLE_DELETED_MSG = "Role {role_name} removed successfully along with all its associations with login instance profiles and policies"
AWSIAM_USER_LOGIN_PROFILE_ALREADY_DELETED_MSG = "Login profile for user {username} cannot be found"
AWSIAM_USER_LOGIN_PROFILE_ALREADY_EXISTS_MSG = "Login profile for user {username} already exists"
AWSIAM_ROLE_DOES_NOT_EXISTS_MSG = "Name {role_name} cannot be found"
AWSIAM_ROLE_INSTANCE_PROFILE_DOES_NOT_EXISTS_MSG = "Profile {instance_profile_name} cannot be found"
AWSIAM_ROLE_ALREADY_EXISTS_MSG = "Role {role_name} already exists in AWS IAM account. Please provide a valid and distinct role name."
AWSIAM_NO_NEED_TO_REMOVE_ROLE_MSG = "Role {role_name} does not exist in AWS IAM account and hence, can not be removed"
AWSIAM_ROLE_INSTANCE_PROFILE_ALREADY_EXISTS_MSG = (
    "Error occurred while creation of instance profile with name {role_name} because it already exists in AWS IAM account"
)
AWSIAM_ROLE_AND_PROFILE_ALREADY_EXISTS_MSG = (
    "Both role as well as instance profile already exist with the given name {role_name}. Please provide a valid and distinct role name."
)
AWSIAM_POLICY_DOC_TRIMMING_ERROR_MSG = (
    "Error occurred while trimming role policy document for removal of unwanted spaces. Please provide a valid json string in policy document."
)
AWSIAM_ROLE_DOES_NOT_EXIST_MSG = "Role {role_name} does not exist. Hence, policy can not be {policy_status}."
AWSIAM_ACTION_FAILED_MSG = "Action {action_name} failed"
AWSIAM_TIMEOUT = 30
AWSIAM_UNKNOWN_ERROR_MSG = "Unknown error occurred. Please check the asset configuration and|or action parameters"
AWSIAM_UNKNOWN_ERROR_CODE = "Error code unavailable"
AWSIAM_TYPE_ERROR_MSG = (
    "Error occurred while connecting to the AWS IAM server. Please check the asset configuration and|or the action parameters"
)
AWSIAM_ERROR_EC2_ROLE_CREDENTIALS_FAILED = "Failed to get EC2 role credentials"
AWSIAM_ERROR_TEMP_CREDENTIALS_FAILED = "Failed to get temporary credentials: {err}"
AWSIAM_ERROR_BAD_ASSET_CONFIG = "Please provide access keys or select assume role check box in asset configuration"
