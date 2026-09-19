"""Config flow for NosAlert integration."""

from typing import Any
import aiohttp
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.selector import (
    SelectSelector,
    SelectSelectorConfig,
    SelectSelectorMode,
)

from .const import (
    API_ACTIVE_ALERTS_URL,
    CONF_API_TOKEN,
    CONF_LOCATIONS,
    DOMAIN,
)
from .locations import LOCATIONS, LocationType

REGION_OPTIONS = [
    str(loc["uid"]) for loc in LOCATIONS
    if loc["type"] in (LocationType.OBLAST, LocationType.SPECIAL_CITY)
]


async def validate_api_token(token: str) -> bool:
    """Validate the API token by performing a test HTTP request."""
    headers = {"Authorization": f"Bearer {token}"}
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(API_ACTIVE_ALERTS_URL, headers=headers, timeout=10) as resp:
                return resp.status in (200, 304)
        except Exception:
            return False


class NosAlertConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for NosAlert."""

    VERSION = 2

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial setup step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            token = user_input[CONF_API_TOKEN].strip()
            locations_input = user_input.get(CONF_LOCATIONS, [])
            if isinstance(locations_input, str):
                locations_input = [loc.strip() for loc in locations_input.split(",") if loc.strip()]

            is_valid = await validate_api_token(token)
            if not is_valid:
                errors["base"] = "invalid_auth"
            elif not locations_input:
                errors["base"] = "no_locations"
            else:
                await self.async_set_unique_id(f"nos_alert_{token[:8]}")
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title="NosAlert",
                    data={
                        CONF_API_TOKEN: token,
                        CONF_LOCATIONS: locations_input,
                    },
                )

        schema = vol.Schema(
            {
                vol.Required(CONF_API_TOKEN): str,
                vol.Required(CONF_LOCATIONS, default=["31"]): SelectSelector(
                    SelectSelectorConfig(
                        options=REGION_OPTIONS,
                        multiple=True,
                        mode=SelectSelectorMode.DROPDOWN,
                        translation_key="locations",
                    )
                ),
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> config_entries.OptionsFlow:
        """Get the options flow for this handler."""
        return NosAlertOptionsFlowHandler(config_entry)


class NosAlertOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for NosAlert."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        self._config_entry = config_entry

    @property
    def config_entry(self) -> config_entries.ConfigEntry:
        """Return the config entry."""
        if hasattr(super(), "config_entry") and super().config_entry is not None:
            return super().config_entry
        return self._config_entry


    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options for NosAlert."""
        if user_input is not None:
            locations_input = user_input.get(CONF_LOCATIONS, [])
            if isinstance(locations_input, str):
                locations_input = [loc.strip() for loc in locations_input.split(",") if loc.strip()]

            # Update entry data
            self.hass.config_entries.async_update_entry(
                self.config_entry,
                data={
                    **self.config_entry.data,
                    CONF_LOCATIONS: locations_input,
                },
            )
            return self.async_create_entry(title="", data={})

        current_locations = self.config_entry.data.get(CONF_LOCATIONS, ["31"])

        schema = vol.Schema(
            {
                vol.Required(CONF_LOCATIONS, default=current_locations): SelectSelector(
                    SelectSelectorConfig(
                        options=REGION_OPTIONS,
                        multiple=True,
                        mode=SelectSelectorMode.DROPDOWN,
                        translation_key="locations",
                    )
                ),
            }
        )

        return self.async_show_form(
            step_id="init",
            data_schema=schema,
        )
