#!/usr/bin/python
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example gets all user team associations.

To create user team associations, run create_user_team_assocations.py.

The LoadFromStorage method is pulling credentials and properties from a
"googleads.yaml" file. By default, it looks for this file in your home
directory. For more information, see the "Caching authentication information"
section of our README.

Tags: UserTeamAssociationService.getUserTeamAssociationsByStatement
"""

__author__ = ('Nicholas Chen',
              'Joseph DiLallo')

# Import appropriate modules from the client library.
from googleads import dfp


def main(client):
  # Initialize appropriate service.
  user_team_association_service = client.GetService(
      'UserTeamAssociationService', version='v201408')

  # Create a filter statement.
  statement = dfp.FilterStatement()

  # Get user team associations by statement.
  while True:
    response = user_team_association_service.getUserTeamAssociationsByStatement(
        statement.ToStatement())
    if 'results' in response:
      # Display results.
      for user_team_association in response['results']:
        print ('User team association between user with ID \'%s\' and team with'
               ' ID \'%s\' was found.' % (user_team_association['userId'],
                                          user_team_association['teamId']))
      statement.offset += dfp.SUGGESTED_PAGE_LIMIT
    else:
      break

  print '\nNumber of results found: %s' % response['totalResultSetSize']


if __name__ == '__main__':
  # Initialize client object.
  dfp_client = dfp.DfpClient.LoadFromStorage()
  main(dfp_client)
