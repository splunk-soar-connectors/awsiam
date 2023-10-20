[comment]: # "Auto-generated SOAR connector documentation"
# AWS IAM

Publisher: Splunk  
Connector Version: 2.1.6  
Product Vendor: AWS  
Product Name: AWS Identity Access Management  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 5.5.0  

This app integrates with Amazon Web Services Identity Access Management (AWS IAM) to support various containment, corrective and investigate actions

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a AWS Identity Access Management asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**access_key** |  optional  | password | Access key ID
**secret_key** |  optional  | password | Secret access key
**use_role** |  optional  | boolean | Use attached role when running Phantom in EC2

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[get user](#action-get-user) - Get details of all the groups and attached policies for the user  
[list groups](#action-list-groups) - List groups of AWS IAM  
[list users](#action-list-users) - List users of AWS IAM  
[list roles](#action-list-roles) - List roles available in AWS IAM  
[add user](#action-add-user) - Add user to a group  
[remove user](#action-remove-user) - Remove user from a group  
[delete user](#action-delete-user) - Delete user from AWS IAM account  
[disable user](#action-disable-user) - Disable login profile and access keys of a user  
[enable user](#action-enable-user) - Enable login profile and access keys of a user  
[add role](#action-add-role) - Add new role in AWS IAM account  
[remove role](#action-remove-role) - Remove role from AWS IAM account  
[attach policy](#action-attach-policy) - Attach managed policy to a role  
[detach policy](#action-detach-policy) - Detach managed policy from a role  
[assign policy](#action-assign-policy) - Assign managed policy to the user  
[remove policy](#action-remove-policy) - Remove managed policy association with the user  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'get user'
Get details of all the groups and attached policies for the user

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username | string |  `user name`  `aws iam user name` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.username | string |  `user name`  `aws iam user name`  |   testUser 
action_result.data.\*.AttachedPolicies.\*.PolicyArn | string |  `aws iam policy arn`  |   arn:aws:iam::123456789012:policy/testPolicy 
action_result.data.\*.AttachedPolicies.\*.PolicyName | string |  |   testPolicy 
action_result.data.\*.AttachedPolicies.\*.RequestId | string |  |   abcd1234-12ab-ab12-ab12-abcdef123456 
action_result.data.\*.Groups.\*.Arn | string |  |   arn:aws:iam::123456789012:group/Test-Group 
action_result.data.\*.Groups.\*.CreateDate | string |  |   2018-05-01T16:44:05Z 
action_result.data.\*.Groups.\*.GroupId | string |  |   ABCDEFGHI1234567890 
action_result.data.\*.Groups.\*.GroupName | string |  `aws iam group name`  |   Test-Group 
action_result.data.\*.Groups.\*.Path | string |  `aws iam group path`  |   /  /testrepo/  /resource_management/test/ 
action_result.data.\*.Groups.\*.RequestId | string |  |   abcd1234-ab12-12ab-ab12-abcdef123456 
action_result.summary.total_groups | numeric |  |   2 
action_result.summary.total_policies | numeric |  |   2 
action_result.message | string |  |   Total policies: 2, Total groups: 2 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
action_result.parameter.credentials | string |  `aws credentials`  |   {'AccessKeyId': 'REDACTED', 'Expiration': 'REDACTED', 'SecretAccessKey': 'REDACTED', 'SessionToken': 'REDACTED'}   

## action: 'list groups'
List groups of AWS IAM

Type: **investigate**  
Read only: **True**

By default groups from path '/' are fetched.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**group_path** |  optional  | Group path in AWS IAM | string |  `aws iam group path` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.group_path | string |  `aws iam group path`  |   /  /testrepo/  /resource_management/test/ 
action_result.data.\*.Arn | string |  |   arn:aws:iam::123456789012:group/Test-Group 
action_result.data.\*.CreateDate | string |  |   2018-05-01T16:44:05Z 
action_result.data.\*.GroupId | string |  |   ABCDEFGHI1234567890 
action_result.data.\*.GroupName | string |  `aws iam group name`  |   Test-Group 
action_result.data.\*.Path | string |  `aws iam group path`  |   /  /testrepo/  /resource_management/test/ 
action_result.data.\*.RequestId | string |  |   abcd1232-ab12-12ab-ab12-abcd1234 
action_result.summary.total_groups | numeric |  |   4 
action_result.message | string |  |   Total groups: 4 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
action_result.parameter.credentials | string |  `aws credentials`  |   {'AccessKeyId': 'REDACTED', 'Expiration': 'REDACTED', 'SecretAccessKey': 'REDACTED', 'SessionToken': 'REDACTED'}   

## action: 'list users'
List users of AWS IAM

Type: **investigate**  
Read only: **True**

If both parameters are provided, users belonging to specified group and to specified path are fetched. If only user path or group name is provided, users belonging to specified path or group respectively are fetched. If no parameters are provided, users belonging to default user path '/' are fetched.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**user_path** |  optional  | Path of the user | string |  `aws iam user path` 
**group_name** |  optional  | Group name | string |  `aws iam group name` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.group_name | string |  `aws iam group name`  |   Test-Group 
action_result.parameter.user_path | string |  `aws iam user path`  |   /  /testrepo/  /resource_management_users/test/ 
action_result.data.\*.Arn | string |  |   arn:aws:iam::123456789012:user/testUser 
action_result.data.\*.CreateDate | string |  |   2018-06-01T18:51:57Z 
action_result.data.\*.PasswordLastUsed | string |  |   2018-08-01T09:09:10Z 
action_result.data.\*.Path | string |  `aws iam user path`  |   /  /testrepo/  /resource_management_users/test/ 
action_result.data.\*.RequestId | string |  |   abcd1234-ab12-ab12-ab12-abcdef123456 
action_result.data.\*.UserId | string |  |   ABCDEFGHI1234567890 
action_result.data.\*.UserName | string |  `user name`  `aws iam user name`  |   testUser 
action_result.summary.total_users | numeric |  |   10 
action_result.message | string |  |   Total users: 10 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
action_result.parameter.credentials | string |  `aws credentials`  |   {'AccessKeyId': 'REDACTED', 'Expiration': 'REDACTED', 'SecretAccessKey': 'REDACTED', 'SessionToken': 'REDACTED'}   

## action: 'list roles'
List roles available in AWS IAM

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.data.\*.Arn | string |  |   arn:aws:iam::123456789012:role/user-role-ExecutionRole 
action_result.data.\*.AssumeRolePolicyDocument | string |  `aws iam role policy doc`  |   {"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":"support.amazonaws.com"},"Action":"sts:AssumeRole"}]} 
action_result.data.\*.CreateDate | string |  |   2018-05-01T20:22:38Z 
action_result.data.\*.Description | string |  |   Ready only access for Redlock to do its thing and generate test data. 
action_result.data.\*.MaxSessionDuration | string |  |   2700 
action_result.data.\*.Path | string |  `aws iam role path`  |   /  /testrepo/  /test-role-path/role-test-path/ 
action_result.data.\*.RequestId | string |  |   1234abcd-12ab-ab12-ab12-123456abcdef 
action_result.data.\*.RoleId | string |  |   ABCDEFGHI1234567890 
action_result.data.\*.RoleName | string |  `aws iam role name`  |   user-role-ExecutionRole 
action_result.summary.total_roles | numeric |  |   11 
action_result.message | string |  |   Total roles: 11 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
action_result.parameter.credentials | string |  `aws credentials`  |   {'AccessKeyId': 'REDACTED', 'Expiration': 'REDACTED', 'SecretAccessKey': 'REDACTED', 'SessionToken': 'REDACTED'}   

## action: 'add user'
Add user to a group

Type: **correct**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username | string |  `user name`  `aws iam user name` 
**group_name** |  required  | Group name | string |  `aws iam group name` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.group_name | string |  `aws iam group name`  |   Test-Group 
action_result.parameter.username | string |  `user name`  `aws iam user name`  |   testUser 
action_result.data.\*.RequestId | string |  |   123456ab-abcd-1234-ab12-abcdef1234 
action_result.summary | string |  |  
action_result.message | string |  |   User testUser successfully added to the group Test-Group 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
action_result.parameter.credentials | string |  `aws credentials`  |   {'AccessKeyId': 'REDACTED', 'Expiration': 'REDACTED', 'SecretAccessKey': 'REDACTED', 'SessionToken': 'REDACTED'}   

## action: 'remove user'
Remove user from a group

Type: **contain**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username | string |  `user name`  `aws iam user name` 
**group_name** |  required  | Group name | string |  `aws iam group name` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.group_name | string |  `aws iam group name`  |   Test-Group 
action_result.parameter.username | string |  `user name`  `aws iam user name`  |   testUser 
action_result.data.\*.RequestId | string |  |   123abcde-abcd-ab34-12cd-12345abcdef 
action_result.summary | string |  |  
action_result.message | string |  |   User testUser successfully removed from the group Test-Group 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
action_result.parameter.credentials | string |  `aws credentials`  |   {'AccessKeyId': 'REDACTED', 'Expiration': 'REDACTED', 'SecretAccessKey': 'REDACTED', 'SessionToken': 'REDACTED'}   

## action: 'delete user'
Delete user from AWS IAM account

Type: **generic**  
Read only: **False**

Delete user and user profile as well as all its associations with groups, policies, and access keys from AWS IAM account.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username | string |  `user name`  `aws iam user name` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.username | string |  `user name`  `aws iam user name`  |   testUser 
action_result.data.\*.RequestId | string |  |   abcd1234-aa11-bb11-cc11-123456abcdef 
action_result.summary | string |  |  
action_result.message | string |  |   User testUser deleted successfully along with all its associations with login profile, access keys, groups, and policies 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
action_result.parameter.credentials | string |  `aws credentials`  |   {'AccessKeyId': 'REDACTED', 'Expiration': 'REDACTED', 'SecretAccessKey': 'REDACTED', 'SessionToken': 'REDACTED'}   

## action: 'disable user'
Disable login profile and access keys of a user

Type: **contain**  
Read only: **False**

If disable access keys parameter is marked false, only login profile is disabled. By default both are disabled.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username | string |  `user name`  `aws iam user name` 
**disable_access_keys** |  optional  | Disable access keys | boolean | 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.disable_access_keys | boolean |  |   True  False 
action_result.parameter.username | string |  `user name`  `aws iam user name`  |   testUser 
action_result.data.\*.RequestId | string |  |   abcd1234-ab12-ab12-ab12-1234abcde 
action_result.summary | string |  |  
action_result.message | string |  |   User testUser disabled successfully 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
action_result.parameter.credentials | string |  `aws credentials`  |   {'AccessKeyId': 'REDACTED', 'Expiration': 'REDACTED', 'SecretAccessKey': 'REDACTED', 'SessionToken': 'REDACTED'}   

## action: 'enable user'
Enable login profile and access keys of a user

Type: **correct**  
Read only: **False**

If enable access keys parameter is marked false, only login profile is enabled. By default both are enabled. If this action is being executed on an already enabled user then other parameters won't affect the action run. <p class="warn">Please exercise caution when using this action. The password may be kept and logged in clear text.</p>

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username | string |  `user name`  `aws iam user name` 
**password** |  required  | Password | string | 
**enable_access_keys** |  optional  | Enable access keys of user along with login profile | boolean | 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.enable_access_keys | boolean |  |   True  False 
action_result.parameter.password | string |  |   testpassword 
action_result.parameter.username | string |  `user name`  `aws iam user name`  |   testUser 
action_result.data.\*.CreateDate | string |  |   2018-08-01T13:45:43Z 
action_result.data.\*.PasswordResetRequired | string |  |   false  true 
action_result.data.\*.RequestId | string |  |   aa216400-a611-11e8-aeae-a514954ff620 
action_result.data.\*.UserName | string |  `user name`  `aws iam user name`  |   testUser 
action_result.summary | string |  |  
action_result.message | string |  |   User testUser enabled successfully 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
action_result.parameter.credentials | string |  `aws credentials`  |   {'AccessKeyId': 'REDACTED', 'Expiration': 'REDACTED', 'SecretAccessKey': 'REDACTED', 'SessionToken': 'REDACTED'}   

## action: 'add role'
Add new role in AWS IAM account

Type: **generic**  
Read only: **False**

Creation of role is a 3 step process. First instance profile is created with the provided role name, then role is created with the same name, and finally the created role is attached with the instance profile created earlier. <p class="warn">Please exercise caution when using this action. Special characters are not allowed in parameter role path.</p>

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**role_name** |  required  | Role name | string |  `aws iam role name` 
**role_policy_document** |  required  | JSON string mentioning trust relationship policy document with the role | string |  `aws iam role policy doc` 
**role_path** |  optional  | Path to the role | string |  `aws iam role path` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.role_name | string |  `aws iam role name`  |   testRole 
action_result.parameter.role_path | string |  `aws iam role path`  |   /  /testRoles/  /testRoles/testRolePath/ 
action_result.parameter.role_policy_document | string |  `aws iam role policy doc`  |   {"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":["ec2.amazonaws.com"]},"Action":["sts:AssumeRole"]}]} 
action_result.data.\*.Arn | string |  |   arn:aws:iam::123456789012:role/test-Role 
action_result.data.\*.AssumeRolePolicyDocument | string |  `aws iam role policy doc`  |   {"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Service":["ec2.amazonaws.com"]},"Action":["sts:AssumeRole"]}]} 
action_result.data.\*.CreateDate | string |  |   2018-08-01T11:45:20Z 
action_result.data.\*.Path | string |  `aws iam role path`  |   /  /testRoles/  /testRoles/testRolePath/ 
action_result.data.\*.RequestId | string |  |   abcd1234-ab12-ab12-ab12-1234abcde 
action_result.data.\*.RoleId | string |  |   ABCDEFGHIJKL12345678 
action_result.data.\*.RoleName | string |  `aws iam role name`  |   test-Role 
action_result.summary | string |  |  
action_result.message | string |  |   Role testRole successfully added in AWS account 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
action_result.parameter.credentials | string |  `aws credentials`  |   {'AccessKeyId': 'REDACTED', 'Expiration': 'REDACTED', 'SecretAccessKey': 'REDACTED', 'SessionToken': 'REDACTED'}   

## action: 'remove role'
Remove role from AWS IAM account

Type: **generic**  
Read only: **False**

Remove role and role instance profiles along with associations of role with all attached policies.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**role_name** |  required  | Role name | string |  `aws iam role name` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.role_name | string |  `aws iam role name`  |   test-Role 
action_result.data.\*.RequestId | string |  |   abcd1234-ab12-ab12-ab12-1234abcde 
action_result.summary | string |  |  
action_result.message | string |  |   Role test-Role removed successfully along with all its associations with login instance profiles and policies 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
action_result.parameter.credentials | string |  `aws credentials`  |   {'AccessKeyId': 'REDACTED', 'Expiration': 'REDACTED', 'SecretAccessKey': 'REDACTED', 'SessionToken': 'REDACTED'}   

## action: 'attach policy'
Attach managed policy to a role

Type: **correct**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**role_name** |  required  | Role name | string |  `aws iam role name` 
**policy_arn** |  required  | Policy ARN | string |  `aws iam policy arn` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.policy_arn | string |  `aws iam policy arn`  |   arn:aws:iam::123456789012:policy/testPolicy 
action_result.parameter.role_name | string |  `aws iam role name`  |   test-Role 
action_result.data.\*.RequestId | string |  |   abcd1234-ab12-ab12-ab12-1234abcde 
action_result.summary | string |  |  
action_result.message | string |  |   Policy with ARN arn:aws:iam::123456789012:policy/testPolicy successfully attached with role test-Role 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
action_result.parameter.credentials | string |  `aws credentials`  |   {'AccessKeyId': 'REDACTED', 'Expiration': 'REDACTED', 'SecretAccessKey': 'REDACTED', 'SessionToken': 'REDACTED'}   

## action: 'detach policy'
Detach managed policy from a role

Type: **contain**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**role_name** |  required  | Role name | string |  `aws iam role name` 
**policy_arn** |  required  | Policy ARN | string |  `aws iam policy arn` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.policy_arn | string |  `aws iam policy arn`  |   arn:aws:iam::123456789012:policy/testPolicy 
action_result.parameter.role_name | string |  `aws iam role name`  |   test-Role 
action_result.data.\*.RequestId | string |  |   abcd1234-ab12-ab12-ab12-1234abcde 
action_result.summary | string |  |  
action_result.message | string |  |   Policy with ARN arn:aws:iam::123456789012:policy/testPolicy successfully detached from role test-Role 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
action_result.parameter.credentials | string |  `aws credentials`  |   {'AccessKeyId': 'REDACTED', 'Expiration': 'REDACTED', 'SecretAccessKey': 'REDACTED', 'SessionToken': 'REDACTED'}   

## action: 'assign policy'
Assign managed policy to the user

Type: **correct**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username | string |  `user name`  `aws iam user name` 
**policy_arn** |  required  | Policy ARN | string |  `aws iam policy arn` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.policy_arn | string |  `aws iam policy arn`  |   arn:aws:iam::123456789012:policy/testpolicy 
action_result.parameter.username | string |  `user name`  `aws iam user name`  |   testUser 
action_result.data.\*.RequestId | string |  |   abcd1234-ab12-ab12-ab12-1234abcde 
action_result.summary | string |  |  
action_result.message | string |  |   Policy with ARN arn:aws:iam::1234567890:policy/testPolicy successfully assigned to user testUser 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
action_result.parameter.credentials | string |  `aws credentials`  |   {'AccessKeyId': 'REDACTED', 'Expiration': 'REDACTED', 'SecretAccessKey': 'REDACTED', 'SessionToken': 'REDACTED'}   

## action: 'remove policy'
Remove managed policy association with the user

Type: **contain**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username | string |  `user name`  `aws iam user name` 
**policy_arn** |  required  | Policy ARN | string |  `aws iam policy arn` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string |  |   success  failed 
action_result.parameter.policy_arn | string |  `aws iam policy arn`  |   arn:aws:iam::123456789012:policy/testPolicy 
action_result.parameter.username | string |  `user name`  `aws iam user name`  |   testUser 
action_result.data.\*.RequestId | string |  |   abcd1234-ab12-ab12-ab12-1234abcde 
action_result.summary | string |  |  
action_result.message | string |  |   Policy with ARN arn:aws:iam::123456789012:policy/testPolicy successfully removed from user testUser 
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 
action_result.parameter.credentials | string |  `aws credentials`  |   {'AccessKeyId': 'REDACTED', 'Expiration': 'REDACTED', 'SecretAccessKey': 'REDACTED', 'SessionToken': 'REDACTED'} 