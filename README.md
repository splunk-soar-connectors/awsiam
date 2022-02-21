[comment]: # "Auto-generated SOAR connector documentation"
# AWS IAM

Publisher: Splunk  
Connector Version: 2\.1\.6  
Product Vendor: AWS  
Product Name: AWS Identity Access Management  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.9\.39220  

This app integrates with Amazon Web Services Identity Access Management \(AWS IAM\) to support various containment, corrective and investigate actions

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a AWS Identity Access Management asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**access\_key** |  optional  | password | Access key ID
**secret\_key** |  optional  | password | Secret access key
**use\_role** |  optional  | boolean | Use attached role when running Phantom in EC2

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
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.username | string |  `user name`  `aws iam user name` 
action\_result\.data\.\*\.AttachedPolicies\.\*\.PolicyArn | string |  `aws iam policy arn` 
action\_result\.data\.\*\.AttachedPolicies\.\*\.PolicyName | string | 
action\_result\.data\.\*\.AttachedPolicies\.\*\.RequestId | string | 
action\_result\.data\.\*\.Groups\.\*\.Arn | string | 
action\_result\.data\.\*\.Groups\.\*\.CreateDate | string | 
action\_result\.data\.\*\.Groups\.\*\.GroupId | string | 
action\_result\.data\.\*\.Groups\.\*\.GroupName | string |  `aws iam group name` 
action\_result\.data\.\*\.Groups\.\*\.Path | string |  `aws iam group path` 
action\_result\.data\.\*\.Groups\.\*\.RequestId | string | 
action\_result\.summary\.total\_groups | numeric | 
action\_result\.summary\.total\_policies | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'list groups'
List groups of AWS IAM

Type: **investigate**  
Read only: **True**

By default groups from path '/' are fetched\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**group\_path** |  optional  | Group path in AWS IAM | string |  `aws iam group path` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.group\_path | string |  `aws iam group path` 
action\_result\.data\.\*\.Arn | string | 
action\_result\.data\.\*\.CreateDate | string | 
action\_result\.data\.\*\.GroupId | string | 
action\_result\.data\.\*\.GroupName | string |  `aws iam group name` 
action\_result\.data\.\*\.Path | string |  `aws iam group path` 
action\_result\.data\.\*\.RequestId | string | 
action\_result\.summary\.total\_groups | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'list users'
List users of AWS IAM

Type: **investigate**  
Read only: **True**

If both parameters are provided, users belonging to specified group and to specified path are fetched\. If only user path or group name is provided, users belonging to specified path or group respectively are fetched\. If no parameters are provided, users belonging to default user path '/' are fetched\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**user\_path** |  optional  | Path of the user | string |  `aws iam user path` 
**group\_name** |  optional  | Group name | string |  `aws iam group name` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.group\_name | string |  `aws iam group name` 
action\_result\.parameter\.user\_path | string |  `aws iam user path` 
action\_result\.data\.\*\.Arn | string | 
action\_result\.data\.\*\.CreateDate | string | 
action\_result\.data\.\*\.PasswordLastUsed | string | 
action\_result\.data\.\*\.Path | string |  `aws iam user path` 
action\_result\.data\.\*\.RequestId | string | 
action\_result\.data\.\*\.UserId | string | 
action\_result\.data\.\*\.UserName | string |  `user name`  `aws iam user name` 
action\_result\.summary\.total\_users | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'list roles'
List roles available in AWS IAM

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.data\.\*\.Arn | string | 
action\_result\.data\.\*\.AssumeRolePolicyDocument | string |  `aws iam role policy doc` 
action\_result\.data\.\*\.CreateDate | string | 
action\_result\.data\.\*\.Description | string | 
action\_result\.data\.\*\.MaxSessionDuration | string | 
action\_result\.data\.\*\.Path | string |  `aws iam role path` 
action\_result\.data\.\*\.RequestId | string | 
action\_result\.data\.\*\.RoleId | string | 
action\_result\.data\.\*\.RoleName | string |  `aws iam role name` 
action\_result\.summary\.total\_roles | numeric | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'add user'
Add user to a group

Type: **correct**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username | string |  `user name`  `aws iam user name` 
**group\_name** |  required  | Group name | string |  `aws iam group name` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.group\_name | string |  `aws iam group name` 
action\_result\.parameter\.username | string |  `user name`  `aws iam user name` 
action\_result\.data\.\*\.RequestId | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'remove user'
Remove user from a group

Type: **contain**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username | string |  `user name`  `aws iam user name` 
**group\_name** |  required  | Group name | string |  `aws iam group name` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.group\_name | string |  `aws iam group name` 
action\_result\.parameter\.username | string |  `user name`  `aws iam user name` 
action\_result\.data\.\*\.RequestId | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'delete user'
Delete user from AWS IAM account

Type: **generic**  
Read only: **False**

Delete user and user profile as well as all its associations with groups, policies, and access keys from AWS IAM account\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username | string |  `user name`  `aws iam user name` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.username | string |  `user name`  `aws iam user name` 
action\_result\.data\.\*\.RequestId | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'disable user'
Disable login profile and access keys of a user

Type: **contain**  
Read only: **False**

If disable access keys parameter is marked false, only login profile is disabled\. By default both are disabled\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username | string |  `user name`  `aws iam user name` 
**disable\_access\_keys** |  optional  | Disable access keys | boolean | 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.disable\_access\_keys | boolean | 
action\_result\.parameter\.username | string |  `user name`  `aws iam user name` 
action\_result\.data\.\*\.RequestId | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'enable user'
Enable login profile and access keys of a user

Type: **correct**  
Read only: **False**

If enable access keys parameter is marked false, only login profile is enabled\. By default both are enabled\. If this action is being executed on an already enabled user then other parameters won't affect the action run\. <p class="warn">Please exercise caution when using this action\. The password may be kept and logged in clear text\.</p>

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username | string |  `user name`  `aws iam user name` 
**password** |  required  | Password | string | 
**enable\_access\_keys** |  optional  | Enable access keys of user along with login profile | boolean | 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.enable\_access\_keys | boolean | 
action\_result\.parameter\.password | string | 
action\_result\.parameter\.username | string |  `user name`  `aws iam user name` 
action\_result\.data\.\*\.CreateDate | string | 
action\_result\.data\.\*\.PasswordResetRequired | string | 
action\_result\.data\.\*\.RequestId | string | 
action\_result\.data\.\*\.UserName | string |  `user name`  `aws iam user name` 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'add role'
Add new role in AWS IAM account

Type: **generic**  
Read only: **False**

Creation of role is a 3 step process\. First instance profile is created with the provided role name, then role is created with the same name, and finally the created role is attached with the instance profile created earlier\. <p class="warn">Please exercise caution when using this action\. Special characters are not allowed in parameter role path\.</p>

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**role\_name** |  required  | Role name | string |  `aws iam role name` 
**role\_policy\_document** |  required  | JSON string mentioning trust relationship policy document with the role | string |  `aws iam role policy doc` 
**role\_path** |  optional  | Path to the role | string |  `aws iam role path` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.role\_name | string |  `aws iam role name` 
action\_result\.parameter\.role\_path | string |  `aws iam role path` 
action\_result\.parameter\.role\_policy\_document | string |  `aws iam role policy doc` 
action\_result\.data\.\*\.Arn | string | 
action\_result\.data\.\*\.AssumeRolePolicyDocument | string |  `aws iam role policy doc` 
action\_result\.data\.\*\.CreateDate | string | 
action\_result\.data\.\*\.Path | string |  `aws iam role path` 
action\_result\.data\.\*\.RequestId | string | 
action\_result\.data\.\*\.RoleId | string | 
action\_result\.data\.\*\.RoleName | string |  `aws iam role name` 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'remove role'
Remove role from AWS IAM account

Type: **generic**  
Read only: **False**

Remove role and role instance profiles along with associations of role with all attached policies\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**role\_name** |  required  | Role name | string |  `aws iam role name` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.role\_name | string |  `aws iam role name` 
action\_result\.data\.\*\.RequestId | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'attach policy'
Attach managed policy to a role

Type: **correct**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**role\_name** |  required  | Role name | string |  `aws iam role name` 
**policy\_arn** |  required  | Policy ARN | string |  `aws iam policy arn` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.policy\_arn | string |  `aws iam policy arn` 
action\_result\.parameter\.role\_name | string |  `aws iam role name` 
action\_result\.data\.\*\.RequestId | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'detach policy'
Detach managed policy from a role

Type: **contain**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**role\_name** |  required  | Role name | string |  `aws iam role name` 
**policy\_arn** |  required  | Policy ARN | string |  `aws iam policy arn` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.policy\_arn | string |  `aws iam policy arn` 
action\_result\.parameter\.role\_name | string |  `aws iam role name` 
action\_result\.data\.\*\.RequestId | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'assign policy'
Assign managed policy to the user

Type: **correct**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username | string |  `user name`  `aws iam user name` 
**policy\_arn** |  required  | Policy ARN | string |  `aws iam policy arn` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.policy\_arn | string |  `aws iam policy arn` 
action\_result\.parameter\.username | string |  `user name`  `aws iam user name` 
action\_result\.data\.\*\.RequestId | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials`   

## action: 'remove policy'
Remove managed policy association with the user

Type: **contain**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | Username | string |  `user name`  `aws iam user name` 
**policy\_arn** |  required  | Policy ARN | string |  `aws iam policy arn` 
**credentials** |  optional  | Assumed role credentials | string |  `aws credentials` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.policy\_arn | string |  `aws iam policy arn` 
action\_result\.parameter\.username | string |  `user name`  `aws iam user name` 
action\_result\.data\.\*\.RequestId | string | 
action\_result\.summary | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.parameter\.credentials | string |  `aws credentials` 