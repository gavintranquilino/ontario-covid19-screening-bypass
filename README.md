# ONTARIO COVID-19 SCREENING TOOL BYPASS

This is a simple tool to bypass the [Ontario COVID-19 Screening Tool](https://covid-19.ontario.ca/school-screening/). A list of contacts can be emailed the results to avoid the need to fill out the form. 

This project is **not** intended to be used to avoid the COVID-19 guidelines, but instead a small project to generate valid results. Please **do not** use this tool to get into school or work if you are ineligible to go in public. Make sure you are following the [guidelines](https://covid-19.ontario.ca/) if you are sick.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the tool.

```bash
pip install https://github.com/GuhBean/ontario-covid19-screening-bypass.git
```

Alternatively, download this project as a **.zip** file, and extract into your device.

## Usage

### config.json
1. Rename **config-sample.json** to **config.json**
2. Enter the *email* and its *password* into the config.json file

```json
{
    "address": "bot email address",
    "password": "bot email password"
}
```

### contacts.txt
1. Locate **contacts-sample.txt** in the *templates* folder
2. Rename **contacts-sample.txt** to *contacts.txt*
3. Fill the text file with the *name of the recipient* and the *respective email address*

```
firstname name@website.domain
firstname name@website.domain
firstname name@website.domain
firstname name@website.domain
firstname name@website.domain
```

### message.txt
1. Locate **message-sample.txt** file in the *templates* folder
2. Rename **message-sample.txt** to **message.txt**
3. Fill the text file with the message you want to send

```
Hello ${PERSON_NAME},

Here is your COVID-19 screening validation.

From,
Bot
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

See [CONTRIBUTING.md](https://github.com/GuhBean/ontario-covid19-screening-bypass/blob/master/CONTRIBUTE.md) file.

## License
See [LICENSE](https://github.com/GuhBean/ontario-covid19-screening-bypass/blob/master/LICENSE) file.