#!/bin/bash
curl -o ct.json https://reestr.rublacklist.net/api/v3/ct-domains/
jq -c 'map({key:.,value:1})|from_entries' ct.json> ctset.json
