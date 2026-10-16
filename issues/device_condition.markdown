Add [device condition](https://contributors.home-assistant.io/core/integrations/device-automations/) support to the {{ DOMAIN }} integration.

Device conditions are part of [Device Automations](https://contributors.home-assistant.io/core/integrations/device-automations/), a new concept that was [recently launched](https://www.home-assistant.io/blog/2019/09/18/release-99/#device-automations) to make automations more user friendly.

Device automations consist of three different parts: triggers, conditions and conditions. This issue is about the condition part.

To get started with this issue, you will need to set up a Home Assistant development environment. The easiest approach is to get started using [a dev container](https://contributors.home-assistant.io/core/development/environment/#development-container).

Once you have a development environment set up, run the following and follow the instructions:

```python
python3 -m script.scaffold device_condition
```

_(This issue is part of #26994)_
