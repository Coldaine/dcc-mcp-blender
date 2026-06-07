class BlenderAddonVersionUpdater {
  updateContent(content, version) {
    const [major, minor, patch] = version.split('.');
    content = content.replace(
      /(__addon_version__\s*=\s*")\d+\.\d+\.\d+(")/,
      `$1${version}$2`,
    );
    // Use arrow function to avoid $1 + digit ambiguity ($10 vs $1+0)
    content = content.replace(
      /("version":\s*\()\d+,\s*\d+,\s*\d+(\))/,
      (_match, prefix, suffix) => `${prefix}${major}, ${minor}, ${patch}${suffix}`,
    );
    return content;
  }
}

module.exports = BlenderAddonVersionUpdater;
