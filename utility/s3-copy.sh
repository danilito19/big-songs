
# terminal command to copy data to S3 for a range of folders
# very slow command!
ls -R . | awk '
/:$/&&f{s=$0;f=0}
/:$/&&!f{sub(/:$/,"");s=$0;f=1;next}
NF&&f{ print s"/"$0 }' | grep -i "\/[Z]\/.\/.\/\w*\.h5" | xargs -I {} aws s3 cp {} s3://songs-data-all


# instead, transfer data to folder inside instance 
ls -R . | awk '
/:$/&&f{s=$0;f=0}
/:$/&&!f{sub(/:$/,"");s=$0;f=1;next}
NF&&f{ print s"/"$0 }'| grep -i ".h5" | xargs -I {} cp {} ../../all_data

#now copy all folder contents to S3
aws s3 cp ./ s3://songs-data-all --recursive

## terminal command for counting objects in bucket
aws s3 ls s3://songs-data-all/ --recursive | wc -l 


